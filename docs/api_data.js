define({ "api": [
  {
    "type": "get",
    "url": "/",
    "title": "Home route",
    "version": "0.1.0",
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
    "filename": "./routes/main.py",
    "groupTitle": "General"
  },
  {
    "type": "post",
    "url": "/person/:id",
    "title": "Get person",
    "version": "0.1.0",
    "name": "GetPerson",
    "group": "Person",
    "description": "<p>Get Person by id</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "id",
            "optional": false,
            "field": "name",
            "description": "<p>The unique id of the person</p>"
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
            "type": "Object",
            "optional": false,
            "field": "data",
            "description": "<p>The <code>person</code> object</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"status\": 200,\n    \"data\": {\n        \"name\": \"treta\",\n        \"Sonas\": [],\n        \"idx\": 9\n    }\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./routes/person.py",
    "groupTitle": "Person"
  },
  {
    "type": "post",
    "url": "/person",
    "title": "New person",
    "version": "0.1.0",
    "name": "PostPerson",
    "group": "Person",
    "description": "<p>Add a new person</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "name",
            "description": "<p>The unique name of the person</p>"
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
            "type": "Object",
            "optional": false,
            "field": "data",
            "description": "<p>The <code>person</code> object</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"status\": 200,\n    \"data\": {\n        \"name\": \"treta\",\n        \"Sonas\": [],\n        \"idx\": 9\n    }\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./routes/person.py",
    "groupTitle": "Person"
  },
  {
    "type": "get",
    "url": "/person",
    "title": "Get all people",
    "version": "0.1.0",
    "name": "getPeople",
    "group": "Person",
    "description": "<p>Get all people on the database</p>",
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
            "type": "Object",
            "optional": false,
            "field": "data",
            "description": "<p>A list of <code>person</code> objects</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    \"status\": 200,\n    \"data\": [{\n        \"name\": \"treta\",\n        \"Sonas\": [],\n        \"idx\": 9\n    }]\n}",
          "type": "json"
        }
      ]
    },
    "filename": "./routes/person.py",
    "groupTitle": "Person"
  },
  {
    "type": "get",
    "url": "/yiff",
    "title": "Yiff route",
    "version": "0.1.0",
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
    "filename": "./docs/main.js",
    "group": "_home_k4t0mono_projs_probable_palm_tree_docs_main_js",
    "groupTitle": "_home_k4t0mono_projs_probable_palm_tree_docs_main_js",
    "name": ""
  }
] });
