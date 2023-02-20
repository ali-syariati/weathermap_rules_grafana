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
                },
                {
                    "hidden": False,
                    "pattern": "qepA3EpPfLnxbVJNl7Fr-516",
                    "textOn": "wmd",
                    "textPattern": "/speed/",
                    "textReplace": "pattern",
                },
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
                },
                {
                    "colorOn": "n",
                    "hidden": False,
                    "pattern": "qepA3EpPfLnxbVJNl7Fr-516",
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

template_rules_update_time = {
    "aggregation": "last_time",
    "alias": "update data",
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
                    "pattern": "6",
                    "textOn": "wmd",
                    "textPattern": "/dateinfo/",
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
    "order": 219,
    "overlayIcon": False,
    "pattern": "/.*/",
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
    "type": "date",
    "unit": "short",
    "valueData": [],
}

template_rules_update_name = [
    {
        "aggregation": "current",
        "alias": "update time",
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
                        "pattern": "4",
                        "textOn": "wmd",
                        "textPattern": "/dateinfo/",
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
        "order": 220,
        "overlayIcon": False,
        "pattern": "updated",
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
        "type": "date",
        "unit": "short",
        "valueData": [],
    },
    {
        "aggregation": "current",
        "alias": "update name",
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
                        "pattern": "4",
                        "textOn": "wmd",
                        "textPattern": "/name/",
                        "textReplace": "pattern",
                    }
                ],
                "options": {"enableRegEx": True, "identByProp": "id", "metadata": ""},
            },
        },
        "metricType": "serie",
        "newRule": False,
        "numberTHData": [
            {"color": "rgba(245, 54, 54, 0.9)", "comparator": "ge", "level": 0},
            {
                "color": "rgba(237, 129, 40, 0.89)",
                "comparator": "ge",
                "level": 0,
                "value": 50,
            },
            {
                "color": "rgba(50, 172, 45, 0.97)",
                "comparator": "ge",
                "level": 0,
                "value": 80,
            },
        ],
        "order": 221,
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
            }
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
        "type": "string",
        "unit": "short",
        "valueData": [],
    },
]

template_query_zabbix = {
    "application": {"filter": ""},
    "datasource": {"type": "alexanderzobnin-zabbix-datasource", "uid": "gHQN77VVz"},
    "functions": [],
    "group": {"filter": "Jateng/Cisco"},
    "hide": False,
    "host": {"filter": "221.132.196.39 ran-pag-gplyen.2"},
    "item": {"filter": "/.*speed|.*Percentage out/"},
    "itemTag": {"filter": "/description:.*(po1_po1|gi0/5/7_gi0/2/0/0).*/"},
    "options": {
        "disableDataAlignment": False,
        "showDisabledItems": False,
        "skipEmptyValues": False,
        "useZabbixValueMapping": False,
    },
    "proxy": {"filter": ""},
    "queryType": "0",
    "refId": "221.132.196.39 ran-pag-gplyen.2",
    "resultFormat": "time_series",
    "table": {"skipEmptyValues": False},
    "tags": {"filter": ""},
    "trigger": {"filter": ""},
    "triggers": {"acknowledged": 2, "count": True, "minSeverity": 3},
}

template_query_grafana = [
    {
        "datasource": {"uid": "P4eTw6hVz"},
        "format": "time_series",
        "group": [],
        "hide": False,
        "metricColumn": "none",
        "rawQuery": True,
        "rawSql": "SELECT \n\t\"time\",\n\tupdated\nFROM \n\t(SELECT\n\t  updated AS \"time\",\n\t  extract(epoch from updated - interval '7 hours') AS utc_time,\n\t  to_char(updated,'yyyy-mm-dd HH24:MI') as updated\n\tFROM dashboard\n\tWHERE title = '{dashboard_name}'\n\t) AS fd\nORDER BY 1",
        "refId": "dateinfo",
        "select": [[{"params": ["value_double"], "type": "column"}]],
        "table": "test_data",
        "timeColumn": "time_date_time",
        "timeColumnType": "timestamp",
        "where": [{"name": "$__timeFilter", "params": [], "type": "macro"}],
    },
    {
        "datasource": {"uid": "P4eTw6hVz"},
        "format": "time_series",
        "group": [],
        "hide": False,
        "metricColumn": "none",
        "rawQuery": True,
        "rawSql": 'SELECT \n\t"time",\n\tu."name" AS "name" \nFROM \n\t(SELECT \n\t\tupdated AS "time",\n\t\textract(epoch from updated - interval \'7 hours\') AS utc_time,\n\t\tupdated_by\n\tFROM dashboard \n\tWHERE title = \'{dashboard_name}\'\n\t) AS fd\nLEFT JOIN "user" as u\n  ON fd.updated_by = u.id\nORDER BY 1',
        "refId": "update name",
        "select": [[{"params": ["value_double"], "type": "column"}]],
        "table": "test_data",
        "timeColumn": "time_date_time",
        "timeColumnType": "timestamp",
        "where": [{"name": "$__timeFilter", "params": [], "type": "macro"}],
    },
]

template_handle_bug =         {
          "application": {
            "filter": ""
          },
          "datasource": {
            "type": "alexanderzobnin-zabbix-datasource",
            "uid": "gHQN77VVz"
          },
          "functions": [],
          "group": {
            "filter": "CBTA"
          },
          "hide": False,
          "host": {
            "filter": "10.0.90.30 ahz-dns1.telkomsel.co.id"
          },
          "item": {
            "filter": "Temperature"
          },
          "itemTag": {
            "filter": "component: temperature"
          },
          "options": {
            "disableDataAlignment": False,
            "showDisabledItems": False,
            "skipEmptyValues": False,
            "useZabbixValueMapping": False
          },
          "proxy": {
            "filter": ""
          },
          "queryType": "0",
          "refId": "handle_bug",
          "resultFormat": "time_series",
          "table": {
            "skipEmptyValues": False
          },
          "tags": {
            "filter": ""
          },
          "trigger": {
            "filter": ""
          },
          "triggers": {
            "acknowledged": 2,
            "count": True,
            "minSeverity": 3
          }
        }
