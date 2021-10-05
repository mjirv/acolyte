<template>
  <div id='setup-container'  v-if="this.needsSetup">
    <div id='setup-modal'>
        <p id='setup-header'>{{ headers[step] }}</p>
        <p id='setup-desc'>{{ descriptions[step] }}</p>
        <form id='setup-form' v-on:submit.prevent="submit">
          <fieldset v-for="field in fields[step]" :key="field">
            <label v-if="field.type=='select'" v-bind:for="field.name">Database Type:</label>
            <select v-if="field.type=='select'" v-model='apiFields[field.name]' class='setup-input' v-bind:name='field.name' v-bind:placeholder='field.placeholder' >
              <option v-for="option in field.options" :key='option' v-bind:value="option">{{ option }}</option>
            </select>
            <input v-else v-bind:type="field.type" v-model='apiFields[field.name]' class='setup-input' v-bind:placeholder="field.placeholder" />
          </fieldset>
          <button id='submit'>Next</button>
        </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'SetupModal',
  data() {
    return {
      headers: [
        "1. Set a password for your Acolyte instance",
        "2. Enter database credentials",
        "3. Upload a schema.yml file",
        "4. Add some example questions"
      ],
      descriptions: [
        "Choose something memorable but hard to guess. Note that this will be shared with any other users of Acolyte in your organization, so do not use a personal or sensitive password.",
        "Use a READ-ONLY account with usage and select permissions on the schema/tables you want to use. You should also make sure the schema(s) are in the user's search path.",
        "Use a schema.yml from your dbt project. Have multiple schema.yml files? Just concatenate them together and upload as one file.",
        "This is a good way to teach Acolyte synonyms. For example, if \"customers\" = \"users\" for you, a question might be \"how many customers do we have?\" and the SQL might be \"select count(*) from users\"."
      ],
      fields: [
          [{name: "acolytePassword", placeholder: "password", type: "password"}],
          [
            {name: "dbType", placeholder: "Database Type", type: "select", options: ["Redshift", "Postgres", "BigQuery", "Snowflake"]},
            {name: "dbHost", placeholder: "hostname"},
            {name: "dbPort", placeholder: "port"},
            {name: "dbUsername", placeholder: "username"},
            {name: "dbPassword", placeholder: "password", type: "password"},
            {name: "dbDatabase", placeholder: "database name", optional: true}
          ]
      ],

      acolytePassword: "",
      dbType: "",
      dbHost: "",
      dbPort: "",
      dbUsername: "",
      dbPassword: "",
      dbDatabase: "",

      needsSetup: true,

      step: 0,
      apiFields: {},
      apiEndpoints: [
        'acolyte_pw',
        'db_info',
        'db_schema',
        'db_examples'
      ]
    };
  },
  methods: {
    submit() {
      var path = process.env.VUE_APP_API_ENDPOINT + '/setup/' + this.apiEndpoints[this.step] // e.g. 'https://acolyte-api.herokuapp.com/api/setup/';
      var body = this.apiFields
      if(Object.entries(body).filter(el => el.length > 0).length == 0){
        this.apiFields = {};
        this.step += 1;
        return;
      }
      axios.post(path, body)
        .then(() => {
          this.apiFields = {};
          this.step += 1;
          if(this.step > this.headers.length) {
            this.needsSetup = false;
          }
        })
        .catch((error) => {
          alert(error);
        });
    }
  },

  components: {
    
  }
};
</script>