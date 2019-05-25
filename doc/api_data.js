define({ "api": [
  {
    "type": "get",
    "url": "/",
    "title": "Home route",
    "name": "GetHome",
    "group": "General",
    "description": "<p>The route to the main page</p>",
    "examples": [
      {
        "title": "Example usage:",
        "content": "curl -i http://localhost/",
        "type": "json"
      }
    ],
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "code",
            "description": "<p>400</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "message",
            "description": "<p>&quot;I don't think so&quot;</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"code\": 400, \n    \"message\": \"I don't think so\"\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "./routes/main.py",
    "groupTitle": "General"
  },
  {
    "type": "get",
    "url": "/yiff",
    "title": "Yiff route",
    "name": "GetYiff",
    "group": "Yiff",
    "description": "<p>The basic yiff me daddy route</p>",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "code",
            "description": "<p>200</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "message",
            "description": "<p>&quot;Yiff me daddy&quot;</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"code\": 200, \n    \"message\": \"Yiff me daddy\"\n}",
          "type": "json"
        }
      ]
    },
    "examples": [
      {
        "title": "Example usage:",
        "content": "curl -i http://localhost/yiff",
        "type": "json"
      }
    ],
    "version": "0.0.0",
    "filename": "./routes/yiff.py",
    "groupTitle": "Yiff"
  },
  {
    "type": "get",
    "url": "/yiff/:name",
    "title": "Yiff someone",
    "version": "0.1.0",
    "name": "GetYiffName",
    "group": "Yiff",
    "description": "<p>Use this route to yiff someone</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>The name to be yiffed</p>"
          }
        ]
      }
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "Number",
            "optional": false,
            "field": "code",
            "description": "<p>200</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "message",
            "description": "<p>&quot;I like to yiff <code>id</code> UwU&quot;</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"code\": 200, \n    \"message\": \"I like to yiff SHeep UwU\"\n}",
          "type": "json"
        }
      ]
    },
    "examples": [
      {
        "title": "Example usage:",
        "content": "curl -i http://localhost/yiff/:name",
        "type": "json"
      }
    ],
    "filename": "./routes/yiff.py",
    "groupTitle": "Yiff"
  },
  {
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "optional": false,
            "field": "varname1",
            "description": "<p>No type.</p>"
          },
          {
            "group": "Success 200",
            "type": "String",
            "optional": false,
            "field": "varname2",
            "description": "<p>With type.</p>"
          }
        ]
      }
    },
    "type": "",
    "url": "",
    "version": "0.0.0",
    "filename": "./doc/main.js",
    "group": "_home_k4t0mono_projs_probable_palm_tree_doc_main_js",
    "groupTitle": "_home_k4t0mono_projs_probable_palm_tree_doc_main_js",
    "name": ""
  }
] });
