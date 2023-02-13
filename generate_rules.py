import json
import re
from copy import copy
from pprint import pprint

# RULES GLOBAL COLOUR MUST BE IN THE FIRST POSITION
put_on_top = True
generate_rules_only = False
# if generate_rules_only False
# True: there already have global colour, False: there not have any rules
only_update_json = True

# load data
data_json = json.load(open("panel.json"))
list_annotation_data = json.load(open("annotation.json"))

# put your xml map here if you want update it
# if your want update xml GENERATE_RULES_ONLY must False
xml_map = None
if xml_map:
    data_json["panels"][0]["flowchartsData"]["flowcharts"][0]["xml"] = xml_map

total_rules = len(data_json["panels"][0]["rulesData"]["rulesData"])

template_colour_arrow = {
    "colorOn": "a",
    "hidden": False,
    "pattern": "qepA3EpPfLnxbVJNl7Fr-80",
    "style": "fillColor",
}
template_global_colour = {
    "aggregation": "current",
    "alias": "global",
    "column": "Time",
    "dateColumn": "Time",
    "dateFormat": "YYYY-MM-DD HH:mm:ss",
    "dateTHData": [
        {
            "color": "rgba(245, 54, 54, 0.9)",
            "comparator": "ge",
            "level": 0,
            "value": "0d",
        },
        {
            "color": "rgba(237, 129, 40, 0.89)",
            "comparator": "ge",
            "level": 0,
            "value": "-1d",
        },
        {
            "color": "rgba(50, 172, 45, 0.97)",
            "comparator": "ge",
            "level": 0,
            "value": "-1w",
        },
    ],
    "decimals": 2,
    "globalThreshold": True,
    "gradient": False,
    "hidden": False,
    "invert": False,
    "mappingType": 1,
    "mapsDat": {
        "events": {
            "dataList": [],
            "options": {"enableRegEx": True, "identByProp": "id", "metadata": ""},
        },
        "links": {
            "dataList": [],
            "options": {"enableRegEx": True, "identByProp": "id", "metadata": ""},
        },
        "shapes": {
            "dataList": [],
            "options": {"enableRegEx": True, "identByProp": "id", "metadata": ""},
        },
        "texts": {
            "dataList": [],
            "options": {"enableRegEx": True, "identByProp": "id", "metadata": ""},
        },
    },
    "metricType": "serie",
    "newRule": False,
    "numberTHData": [
        {"color": "#ffffffe6", "comparator": "ge", "level": 0, "value": 50},
        {"color": "#A352CC", "comparator": "ge", "level": 0, "value": 1},
        {"color": "#3274D9", "comparator": "ge", "level": 0, "value": 15},
        {"color": "#73BF69", "comparator": "ge", "level": 0, "value": 30},
        {"color": "#FADE2A", "comparator": "ge", "level": 0, "value": 50},
        {"color": "#FF9830", "comparator": "ge", "level": 0, "value": 70},
        {
            "color": "rgba(245, 54, 54, 0.9)",
            "comparator": "ge",
            "level": 0,
            "value": 80,
        },
    ],
    "order": 1,
    "overlayIcon": False,
    "pattern": "name",
    "rangeData": [],
    "reduce": True,
    "refId": "A",
    "sanitize": False,
    "stringTHData": [
        {
            "color": "rgba(245, 54, 54, 0.9)",
            "comparator": "eq",
            "level": 0,
            "value": "/.*/",
        },
        {
            "color": "rgba(237, 129, 40, 0.89)",
            "comparator": "eq",
            "level": 0,
            "value": "/.*warning.*/",
        },
        {
            "color": "rgba(50, 172, 45, 0.97)",
            "comparator": "eq",
            "level": 0,
            "value": "/.*(success|ok).*/",
        },
    ],
    "tooltip": False,
    "tooltipColors": False,
    "tooltipIframe": "",
    "tooltipLabel": "",
    "tooltipOn": "a",
    "tooltipOnlyIframe": False,
    "tpDirection": "v",
    "tpGraph": False,
    "tpGraphScale": "linear",
    "tpGraphSize": "100%",
    "tpGraphType": "line",
    "tpMetadata": False,
    "type": "number",
    "unit": "percent",
    "valueData": [],
}
template_rules_speed = {
    "aggregation": "current",
    "alias": "ran-pag-pklgan.5: Te0/3/0 speed",
    "column": "Time",
    "dateColumn": "Time",
    "dateFormat": "YYYY-MM-DD HH:mm:ss",
    "dateTHData": [
        {
            "color": "rgba(245, 54, 54, 0.9)",
            "comparator": "ge",
            "level": 0,
            "value": "0d",
        },
        {
            "color": "rgba(237, 129, 40, 0.89)",
            "comparator": "ge",
            "level": 0,
            "value": "-1d",
        },
        {
            "color": "rgba(50, 172, 45, 0.97)",
            "comparator": "ge",
            "level": 0,
            "value": "-1w",
        },
    ],
    "decimals": 2,
    "globalThreshold": False,
    "gradient": False,
    "hidden": False,
    "invert": False,
    "mappingType": 1,
    "mapsDat": {
        "events": {
            "dataList": [],
            "options": {"enableRegEx": True, "identByProp": "id", "metadata": ""},
        },
        "links": {
            "dataList": [],
            "options": {"enableRegEx": True, "identByProp": "id", "metadata": ""},
        },
        "shapes": {
            "dataList": [],
            "options": {"enableRegEx": True, "identByProp": "id", "metadata": ""},
        },
        "texts": {
            "dataList": [
                {
                    "hidden": False,
                    "pattern": "qepA3EpPfLnxbVJNl7Fr-516",
                    "textOn": "wmd",
                    "textPattern": "/speed/",
                    "textReplace": "pattern",
                }
            ],
            "options": {"enableRegEx": True, "identByProp": "id", "metadata": ""},
        },
    },
    "metricType": "serie",
    "newRule": False,
    "numberTHData": [
        {"color": "rgba(245, 54, 54, 0.9)", "comparator": "ge", "level": 0}
    ],
    "order": 2,
    "overlayIcon": False,
    "pattern": "221.132.196.62 ran-pag-pklgan.5: Cisco ASAv: Te0/3/0 Link speed",
    "rangeData": [],
    "reduce": True,
    "refId": "A",
    "sanitize": False,
    "stringTHData": [
        {
            "color": "rgba(245, 54, 54, 0.9)",
            "comparator": "eq",
            "level": 0,
            "value": "/.*/",
        },
        {
            "color": "rgba(237, 129, 40, 0.89)",
            "comparator": "eq",
            "level": 0,
            "value": "/.*warning.*/",
        },
        {
            "color": "rgba(50, 172, 45, 0.97)",
            "comparator": "eq",
            "level": 0,
            "value": "/.*(success|ok).*/",
        },
    ],
    "tooltip": False,
    "tooltipColors": False,
    "tooltipIframe": "",
    "tooltipLabel": "",
    "tooltipOn": "a",
    "tooltipOnlyIframe": False,
    "tpDirection": "v",
    "tpGraph": False,
    "tpGraphScale": "linear",
    "tpGraphSize": "100%",
    "tpGraphType": "line",
    "tpMetadata": False,
    "type": "number",
    "unit": "decbytes",
    "valueData": [],
}
template_rules_percent = {
    "aggregation": "current",
    "alias": "ran-pag-pklgan.5 Te0/3/0 Percent",
    "column": "Time",
    "dateColumn": "Time",
    "dateFormat": "YYYY-MM-DD HH:mm:ss",
    "dateTHData": [
        {
            "color": "rgba(245, 54, 54, 0.9)",
            "comparator": "ge",
            "level": 0,
            "value": "0d",
        },
        {
            "color": "rgba(237, 129, 40, 0.89)",
            "comparator": "ge",
            "level": 0,
            "value": "-1d",
        },
        {
            "color": "rgba(50, 172, 45, 0.97)",
            "comparator": "ge",
            "level": 0,
            "value": "-1w",
        },
    ],
    "decimals": 2,
    "globalThreshold": False,
    "gradient": False,
    "hidden": False,
    "invert": False,
    "mappingType": 1,
    "mapsDat": {
        "events": {
            "dataList": [],
            "options": {"enableRegEx": True, "identByProp": "id", "metadata": ""},
        },
        "links": {
            "dataList": [
                {
                    "hidden": False,
                    "linkOn": "a",
                    "linkParams": False,
                    "linkUrl": "https://10.54.68.73/d/_2psXXo4z/ran-pag-pklgan-5-wan_ran_ran-pag-pklgan-5_ran-agg-nusukan-4_te0-3-0_te0-3-0-43_10_fots_otn_huawei_tsel_fiber_l3_osn58-te0-3-0?orgId=1",
                    "pattern": "qepA3EpPfLnxbVJNl7Fr-516",
                },
                {
                    "hidden": False,
                    "linkOn": "a",
                    "linkParams": False,
                    "linkUrl": "https://10.54.68.73/d/_2psXXo4z/ran-pag-pklgan-5-wan_ran_ran-pag-pklgan-5_ran-agg-nusukan-4_te0-3-0_te0-3-0-43_10_fots_otn_huawei_tsel_fiber_l3_osn58-te0-3-0?orgId=1",
                    "pattern": "qepA3EpPfLnxbVJNl7Fr-514",
                },
            ],
            "options": {"enableRegEx": True, "identByProp": "id", "metadata": ""},
        },
        "shapes": {
            "dataList": [
                {
                    "colorOn": "a",
                    "hidden": False,
                    "pattern": "qepA3EpPfLnxbVJNl7Fr-514",
                    "style": "fillColor",
                }
            ],
            "options": {"enableRegEx": True, "identByProp": "id", "metadata": ""},
        },
        "texts": {
            "dataList": [
                {
                    "hidden": False,
                    "pattern": "qepA3EpPfLnxbVJNl7Fr-516",
                    "textOn": "wmd",
                    "textPattern": "/received/",
                    "textReplace": "pattern",
                }
            ],
            "options": {"enableRegEx": True, "identByProp": "id", "metadata": ""},
        },
    },
    "metricType": "serie",
    "newRule": False,
    "numberTHData": [{"color": "#00000000", "comparator": "ge", "level": 0}],
    "order": 3,
    "overlayIcon": False,
    "pattern": "221.132.196.62 ran-pag-pklgan.5: Cisco ASAv: Te0/3/0 Percentage " "out",
    "rangeData": [],
    "reduce": True,
    "refId": "A",
    "sanitize": False,
    "stringTHData": [
        {
            "color": "rgba(245, 54, 54, 0.9)",
            "comparator": "eq",
            "level": 0,
            "value": "/.*/",
        },
        {
            "color": "rgba(237, 129, 40, 0.89)",
            "comparator": "eq",
            "level": 0,
            "value": "/.*warning.*/",
        },
        {
            "color": "rgba(50, 172, 45, 0.97)",
            "comparator": "eq",
            "level": 0,
            "value": "/.*(success|ok).*/",
        },
    ],
    "tooltip": True,
    "tooltipColors": False,
    "tooltipIframe": "<iframe "
    'src="https://10.54.68.73/d-solo/_2psXXo4z/ran-pag-pklgan-5-wan_ran_ran-pag-pklgan-5_ran-agg-nusukan-4_te0-3-0_te0-3-0-43_10_fots_otn_huawei_tsel_fiber_l3_osn58-te0-3-0?orgId=1&panelId=2" '
    'width="600" height="400" frameborder="0"></iframe>',
    "tooltipLabel": "",
    "tooltipOn": "a",
    "tooltipOnlyIframe": True,
    "tpDirection": "v",
    "tpGraph": False,
    "tpGraphScale": "linear",
    "tpGraphSize": "100%",
    "tpGraphType": "line",
    "tpMetadata": False,
    "type": "number",
    "unit": "percent",
    "valueData": [],
}

result_rules = []
result_colour = []
for idx, annotation_data in enumerate(list_annotation_data):
    if annotation_data["alias"] == "":
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
    template_rules_percent["pattern"] = annotation_data["pattern_percentage"]
    template_rules_percent["tooltipIframe"] = annotation_data["iframe"]
    if put_on_top and idx == 0:
        index_rules = 2
    elif not put_on_top and idx == 0:
        index_rules = total_rules + 1
    else:
        index_rules += 1
    template_rules_speed["order"] = index_rules
    index_rules += 1
    template_rules_percent["order"] = index_rules

    # colour
    template_colour_arrow["pattern"] = annotation_data["arrow_id"]

    if generate_rules_only:
        result_rules.append(copy(template_rules_speed))
        result_rules.append(copy(template_rules_percent))
        result_colour.append(copy(template_colour_arrow))
    else:
        if not only_update_json and idx == 0:
            data_json["panels"][0]["rulesData"]["rulesData"][0] = template_global_colour

        if put_on_top:
            data_json["panels"][0]["rulesData"]["rulesData"].insert(
                index_rules - 1, copy(template_rules_speed)
            )
            data_json["panels"][0]["rulesData"]["rulesData"].insert(
                index_rules - 1, copy(template_rules_percent)
            )
        else:
            data_json["panels"][0]["rulesData"]["rulesData"].append(
                copy(template_rules_speed)
            )
            data_json["panels"][0]["rulesData"]["rulesData"].append(
                copy(template_rules_percent)
            )

        data_json["panels"][0]["rulesData"]["rulesData"][0]["mapsDat"]["shapes"][
            "dataList"
        ].append(copy(template_colour_arrow))

if not generate_rules_only and put_on_top:
    for idx in range(len(data_json["panels"][0]["rulesData"]["rulesData"])):
        data_json["panels"][0]["rulesData"]["rulesData"][idx]["order"] = idx


if generate_rules_only:
    write_rules = open("result_rules.json", "w")
    write_colours = open("result_colour.json", "w")
    write_rules.write(json.dumps(result_rules, indent=2))
    write_colours.write(json.dumps(result_colour, indent=2))
    write_rules.close()
    write_colours.close()
else:
    write_panel = open("result_panel.json", "w")
    write_panel.write(json.dumps(data_json, indent=2))
    write_panel.close()
