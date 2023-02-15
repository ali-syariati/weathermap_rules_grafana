import json
import re
from copy import deepcopy

from template import (
    template_colour_arrow,
    template_global_colour,
    template_rules_speed,
    template_rules_percent,
    template_rules_update_time,
    template_rules_update_name,
    template_query_zabbix,
    template_query_grafana,
    template_handle_bug,
)

from pprint import pprint


class Generate_Rules_Grafana(object):
    def __init__(self):
        # True: there already have global colour, False: there not have any rules
        self.update_only = True
        self.put_on_top = True
        self.update_xml = False

        # query init
        self.datasource_type_zabbix = "alexanderzobnin-zabbix-datasource"
        self.datasource_uid_zabbix_collector = "gHQN77VVz"
        self.datasource_uid_grafana = "P4eTw6hVz"

        self.path_xml = "clean_panel_xml.xml"

        self.data_json = json.load(open("panel.json"))
        self.list_annotation_data = json.load(open("annotation.json"))

        if not self.update_only:
            self.annotation_date = json.load(open("annotation_date.json"))

    def update_xml_to_panel(self):
        with open(self.path_xml, "r") as read_file_xml:
            file_xml = re.sub(r'^"|"$|",$', "", read_file_xml.read())
            file_xml = re.sub(r'\\"', '"', file_xml)
        with open("clean_panel_xml.xml", "w") as write_xml:
            write_xml.write(file_xml)
        self.data_json["panels"][0]["flowchartsData"]["flowcharts"][0]["xml"] = file_xml

    def save_result(self, result_rules, result_colour, result_query):
        write_rules = open("result_rules.json", "w")
        write_rules.write(json.dumps(result_rules, indent=2))
        write_rules.close()

        write_colours = open("result_colour.json", "w")
        write_colours.write(json.dumps(result_colour, indent=2))
        write_colours.close()

        write_query = open("result_query.json", "w")
        write_query.write(json.dumps(result_query, indent=2))
        write_query.close()

        write_panel = open("result_panel.json", "w")
        write_panel.write(json.dumps(self.data_json, indent=2))
        write_panel.close()

    def generate_query(self):
        list_query = {}

        list_query = {
            val["refId"]: val for val in self.data_json["panels"][0]["targets"]
        }

        for annotation in self.list_annotation_data:
            host_info = annotation["pattern_percentage"].split(": ")[0]

            if annotation.get("item_tag_filter", "") == "":
                if "description" in annotation["item_tag_filter"]:
                    get_id_tag = max(
                        [
                            val
                            for val in re.findall(
                                r"([a-zA-Z]+\d+(\/\d+)*_[a-zA-Z]+\d+(\/\d+)*)|([a-zA-Z]+(-[a-zA-Z]+)*\d+_[a-zA-Z]+(-[a-zA-Z]+)*\d+)",
                                annotation["item_tag_filter"],
                            )
                        ][0],
                        key=len,
                    )
                elif "interface" in annotation["item_tag_filter"]:
                    get_id_tag = max(
                        [
                            val
                            for val in re.findall(
                                r"(([a-zA-Z]+)(-[a-zA-Z]+)*\d+(\/\d+)*)", annotation["item_tag_filter"]
                            )
                        ][0],
                        key=len,
                    )
            else:
                get_id_tag = annotation["id_tag_filter"]

            if host_info not in list_query:
                template_query_zabbix["datasource"][
                    "type"
                ] = self.datasource_type_zabbix
                template_query_zabbix["datasource"][
                    "uid"
                ] = self.datasource_uid_zabbix_collector
                template_query_zabbix["group"]["filter"] = annotation["group_filter"]
                template_query_zabbix["host"]["filter"] = host_info
                template_query_zabbix["refId"] = host_info
                template_query_zabbix["item"]["filter"] = annotation["item_filter"]
                if "description" in annotation["item_tag_filter"]:
                    template_query_zabbix["itemTag"][
                        "filter"
                    ] = f"/description.*({get_id_tag}).*/"
                elif "interface" in annotation["item_tag_filter"]:
                    template_query_zabbix["itemTag"][
                        "filter"
                    ] = f"/interface.*({get_id_tag})$/"
                list_query[host_info] = deepcopy(template_query_zabbix)
            else:
                regex_filter = list_query[host_info]["itemTag"]["filter"]
                if "description" in annotation["item_tag_filter"]:
                    if (
                        "interface" in list_query[host_info]["itemTag"]["filter"]
                        and "description"
                        not in list_query[host_info]["itemTag"]["filter"]
                    ):
                        list_query[host_info]["itemTag"]["filter"] = list_query[
                            host_info
                        ]["itemTag"]["filter"].replace(
                            ")$/", f")$|description.*({get_id_tag}).*/"
                        )
                    else:
                        list_query[host_info]["itemTag"]["filter"] = list_query[
                            host_info
                        ]["itemTag"]["filter"].replace(").*", f"|{get_id_tag}).*")

                elif "interface" in annotation["item_tag_filter"]:
                    if (
                        "description" in list_query[host_info]["itemTag"]["filter"]
                        and "interface"
                        not in list_query[host_info]["itemTag"]["filter"]
                    ):
                        list_query[host_info]["itemTag"]["filter"] = list_query[
                            host_info
                        ]["itemTag"]["filter"].replace(
                            ").*/", f").*|interface.*({get_id_tag})$/"
                        )
                    else:
                        list_query[host_info]["itemTag"]["filter"] = list_query[
                            host_info
                        ]["itemTag"]["filter"].replace(")$", f"|{get_id_tag})$")

        if self.update_only:
            list_id_query = set(
                val["pattern_percentage"].split(": ")[0]
                for val in self.list_annotation_data
            )
            list_query = [list_query[val] for val in list_id_query if val != "handle_bug"]
            list_query.insert(
                0, template_handle_bug
            )
        else:
            list_id_query = sorted([val for val in list_query if val != "A"], reverse=False)
            list_query = [list_query[val] for val in list_id_query]
            template_query_grafana[0]["rawSql"] = template_query_grafana[0]["rawSql"].replace("{dashboard_name}", self.annotation_date["dashboard_name"])
            template_query_grafana[1]["rawSql"] = template_query_grafana[1]["rawSql"].replace("{dashboard_name}", self.annotation_date["dashboard_name"])
            list_query.extend(deepcopy(template_query_grafana))
            list_query.insert(
                0, template_handle_bug
            )

        return list_query

    def generate_rules(self):
        result_rules = []
        result_colour = []

        total_rules = len(self.data_json["panels"][0]["rulesData"]["rulesData"])

        for idx, annotation_data in enumerate(self.list_annotation_data):
            if annotation_data.get("alias", "") == "":
                annotation_data["alias"] = (
                    re.sub(r"\d+\.\d+\.\d+\.\d+ ", "", annotation_data["pattern_speed"])
                    .replace(": Cisco ASAv", "")
                    .replace(" Link speed", "")
                    .replace(" Percentage out", "")
                )

            # rules
            template_rules_speed["alias"] = annotation_data["alias"] + " Speed"
            template_rules_speed["mapsDat"]["texts"]["dataList"][0][
                "pattern"
            ] = annotation_data["label_id"]
            template_rules_speed["pattern"] = annotation_data["pattern_speed"]
            template_rules_percent["alias"] = annotation_data["alias"] + " Percent"
            template_rules_percent["mapsDat"]["texts"]["dataList"][0][
                "pattern"
            ] = annotation_data["label_id"]
            template_rules_percent["mapsDat"]["links"]["dataList"][0][
                "pattern"
            ] = annotation_data["label_id"]
            template_rules_percent["mapsDat"]["links"]["dataList"][1][
                "pattern"
            ] = annotation_data["arrow_id"]
            template_rules_percent["mapsDat"]["links"]["dataList"][0][
                "linkUrl"
            ] = annotation_data["link_url"]
            template_rules_percent["mapsDat"]["links"]["dataList"][1][
                "linkUrl"
            ] = annotation_data["link_url"]
            template_rules_percent["mapsDat"]["shapes"]["dataList"][0][
                "pattern"
            ] = annotation_data["arrow_id"]
            template_rules_percent["mapsDat"]["shapes"]["dataList"][1][
                "pattern"
            ] = annotation_data["label_id"]
            template_rules_percent["pattern"] = annotation_data["pattern_percentage"]
            template_rules_percent["tooltipIframe"] = annotation_data["iframe"]
            if self.put_on_top and idx == 0:
                index_rules = 2
            elif not self.put_on_top and idx == 0:
                index_rules = total_rules + 1
            else:
                index_rules += 1
            template_rules_speed["order"] = index_rules
            index_rules += 1
            template_rules_percent["order"] = index_rules

            # colour
            template_colour_arrow["pattern"] = annotation_data["arrow_id"]

            result_rules.append(deepcopy(template_rules_speed))
            result_rules.append(deepcopy(template_rules_percent))
            result_colour.append(deepcopy(template_colour_arrow))

            if not self.update_only and idx == 0:
                self.data_json["panels"][0]["rulesData"]["rulesData"] = []
                self.data_json["panels"][0]["rulesData"]["rulesData"].append(template_global_colour)

            if self.put_on_top:
                self.data_json["panels"][0]["rulesData"]["rulesData"].insert(
                    index_rules - 2, deepcopy(template_rules_speed)
                )
                self.data_json["panels"][0]["rulesData"]["rulesData"].insert(
                    index_rules - 2, deepcopy(template_rules_percent)
                )
            else:
                self.data_json["panels"][0]["rulesData"]["rulesData"].append(
                    deepcopy(template_rules_speed)
                )
                self.data_json["panels"][0]["rulesData"]["rulesData"].append(
                    deepcopy(template_rules_percent)
                )

            self.data_json["panels"][0]["rulesData"]["rulesData"][0]["mapsDat"][
                "shapes"
            ]["dataList"].append(deepcopy(template_colour_arrow))

        if self.put_on_top:
            for idx in range(
                len(self.data_json["panels"][0]["rulesData"]["rulesData"])
            ):
                self.data_json["panels"][0]["rulesData"]["rulesData"][idx]["order"] = (
                    idx + 1
                )

        if not self.update_only:
            template_rules_update_time["mapsDat"]["texts"]["dataList"][0][
                "pattern"
            ] = self.annotation_date["lates_data_info"]["rules"]["id_label"]
            template_rules_update_time["mapsDat"]["texts"]["dataList"][0][
                "textPattern"
            ] = self.annotation_date["lates_data_info"]["rules"]["regex_pattern"]
            template_rules_update_time["pattern"] = self.annotation_date["lates_data_info"][
                "regex_pattern"
            ]

            template_rules_update_name[0]["mapsDat"]["texts"]["dataList"][0][
                "pattern"
            ] = self.annotation_date["lates_edit_info"]["rules"]["id_label"]
            template_rules_update_name[0]["mapsDat"]["texts"]["dataList"][0][
                "textPattern"
            ] = self.annotation_date["lates_edit_info"]["rules"]["regex_pattern"]
            template_rules_update_name[0]["pattern"] = self.annotation_date["lates_edit_info"][
                "regex_pattern"
            ]

            template_rules_update_name[1]["mapsDat"]["texts"]["dataList"][0][
                "pattern"
            ] = self.annotation_date["lates_edit_name"]["rules"]["id_label"]
            template_rules_update_name[1]["mapsDat"]["texts"]["dataList"][0][
                "textPattern"
            ] = self.annotation_date["lates_edit_name"]["rules"]["regex_pattern"]
            template_rules_update_name[1]["pattern"] = self.annotation_date["lates_edit_name"][
                "regex_pattern"
            ]

            result_rules.append(deepcopy(template_rules_update_time))
            result_rules.extend(deepcopy(template_rules_update_name))
            self.data_json["panels"][0]["rulesData"]["rulesData"].append(
                deepcopy(template_rules_update_time)
            )
            self.data_json["panels"][0]["rulesData"]["rulesData"].extend(
                deepcopy(template_rules_update_name)
            )

        return result_rules, result_colour

    def main(self):
        if self.update_xml:
            self.update_xml_to_panel()

        result_rules = []
        result_colour = []
        result_query = []

        result_query = self.generate_query()
        if not self.update_only:
            self.data_json["panels"][0]["targets"]=[]
        self.data_json["panels"][0]["targets"].extend(result_query)

        result_rules, result_colour = self.generate_rules()
        self.save_result(result_rules, result_colour, result_query)


if __name__ == "__main__":
    Generate_Rules_Grafana().main()
