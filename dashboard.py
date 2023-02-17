import json

dashboard_query_data = json.load(open('dashboard_query.json'))


def panel_str(
        grid_h: int,
        grid_w: int,
        grid_x: int,
        grid_y: int,
        time_from: str,
        interval: str,
        title_opening: str):
    return {
        "datasource": {
            "type": dashboard_query_data['datasource_type'],
            "uid": dashboard_query_data['datasource_uid_1']
        },
        "fieldConfig": {
            "defaults": {
                "color": {
                    "mode": "palette-classic"
                },
                "custom": {
                    "axisLabel": "",
                    "axisPlacement": "auto",
                    "barAlignment": 0,
                    "drawStyle": "line",
                    "fillOpacity": 9,
                    "gradientMode": "none",
                    "hideFrom": {
                        "legend": False,
                        "tooltip": False,
                        "viz": False
                    },
                    "lineInterpolation": "linear",
                    "lineWidth": 1,
                    "pointSize": 1,
                    "scaleDistribution": {
                        "type": "linear"
                    },
                    "showPoints": "auto",
                    "spanNulls": False,
                    "stacking": {
                        "group": "A",
                        "mode": "none"
                    },
                    "thresholdsStyle": {
                        "mode": "off"
                    }
                },
                "mappings": [],
                "min": 0,
                "thresholds": {
                    "mode": "absolute",
                    "steps": [
                        {
                            "color": "green",
                            "value": None
                        }
                    ]
                },
                "unit": "deckbytes"
            },
            "overrides": [
                {
                    "matcher": {
                        "id": "byName",
                        "options": "Outbound"
                    },
                    "properties": [
                        {
                            "id": "color",
                            "value": {
                                "fixedColor": "dark-blue",
                                "mode": "fixed"
                            }
                        }
                    ]
                },
                {
                    "matcher": {
                        "id": "byName",
                        "options": "Inbound"
                    },
                    "properties": [
                        {
                            "id": "color",
                            "value": {
                                "fixedColor": "dark-green",
                                "mode": "fixed"
                            }
                        }
                    ]
                }
            ]
        },
        "gridPos": {
            "h": grid_h,
            "w": grid_w,
            "x": grid_x,
            "y": grid_y
        },
        "id": None,
        "interval": interval,
        "options": {
            "legend": {
                "calcs": [
                    "lastNotNull",
                    "mean",
                    "max"
                ],
                "displayMode": "table",
                "placement": "bottom"
            },
            "tooltip": {
                "mode": "single",
                "sort": "none"
            }
        },
        "targets": [
            {
                "application": {
                    "filter": ""
                },
                "datasource": {
                    "type": dashboard_query_data['datasource_type'],
                    "uid": dashboard_query_data['datasource_uid_2']
                },
                "functions": [
                    {
                        "def": {
                            "category": "Alias",
                            "defaultParams": [],
                            "name": "setAlias",
                            "params": [
                                {
                                    "name": "alias",
                                    "type": "string"
                                }
                            ]
                        },
                        "params": [
                            "Outbound"
                        ],
                        "text": "setAlias(Outbound)"
                    }
                ],
                "group": {
                    "filter": dashboard_query_data['group_filter']
                },
                "host": {
                    "filter": dashboard_query_data['host_filter']
                },
                "item": {
                    "filter": dashboard_query_data['item_filter_outbound']
                },
                "itemTag": {
                    "filter": dashboard_query_data['item_tag_filter']
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
                "refId": "Outbound",
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
            },
            {
                "application": {
                    "filter": ""
                },
                "datasource": {
                    "type": dashboard_query_data['datasource_type'],
                    "uid": dashboard_query_data['datasource_uid_2']
                },
                "functions": [
                    {
                        "def": {
                            "category": "Alias",
                            "defaultParams": [],
                            "name": "setAlias",
                            "params": [
                                {
                                    "name": "alias",
                                    "type": "string"
                                }
                            ]
                        },
                        "params": [
                            "Inbound"
                        ],
                        "text": "setAlias(Inbound)"
                    }
                ],
                "group": {
                    "filter": dashboard_query_data['group_filter']
                },
                "hide": False,
                "host": {
                    "filter": dashboard_query_data['host_filter']
                },
                "item": {
                    "filter": dashboard_query_data['item_filter_inbound']
                },
                "itemTag": {
                    "filter": dashboard_query_data['item_tag_filter']
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
                "refId": "Inbound",
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
        ],
        "timeFrom": time_from,
        "title": f"{title_opening} {dashboard_query_data['title']}",
        "type": "timeseries"
    }


template_panel = {
    "panels": [
        panel_str(9, 24, 0, 0, '24h', '5m', 'Daily (5 Minute Average)'),
        panel_str(9, 24, 0, 9, '7d', '30m', 'Weekly (30 Minute Average)'),
        panel_str(9, 24, 0, 18, '120d', '2h', 'Monthly (2 Hours Average)'),
        panel_str(9, 27, 0, 27, '360d', '1d', 'Yearly (1 Day Average)')
    ],
    "refresh": "",
    "schemaVersion": 36,
    "style": "dark",
    "tags": [],
    "templating": {
        "list": []
    },
    "time": {
        "from": "now-5m",
        "to": "now"
    },
    "timepicker": {
        "hidden": True
    },
    "timezone": dashboard_query_data['timezone'],
}

write_panel = open("result_panel.json", "w")
write_panel.write(json.dumps(template_panel, indent=2))
write_panel.close()
