<template>
  <div>
    <span id='title'><span id='title-container'><a href='https://www.acolytehq.com' target='_blank'>💡 Acolyte</a></span></span>
    <SetupModal v-if="do_setup" />
    <div class='container'>
      <span id='header'>Question</span>
      <p>
        <em><a href='https://github.com/dbt-labs/jaffle_shop' target='_blank'>Jaffle Shop</a> is a database about jaffle (grilled cheese) sales.
        You can ask questions like "how many customers had 2+ orders?" or "who placed the most recent order?"</em>
      </p>
      <form id='question-form' v-on:submit.prevent="submit">
          <input v-model="question" id='question' autofocus />
          <button title="Submit" id='submit'>Submit</button>
      </form>
    </div>
    <div class='container'>
      <span id='header'>Results</span>
      <div class='data-table'>
        <data-table :rows="data" :striped=true />
      </div>
    </div>
    <div class='container'>
      <span id='header'>SQL</span>
      <div class='data-table'>
        <code class="block whitespace-pre overflow-x-scroll">
          {{ sql_query }}
        </code>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { DataTable } from '@jobinsjp/vue3-datatable';
import SetupModal from './SetupModal.vue'

export default {
  name: 'Question',
  data() {
    return {
      api_endpoint: process.env.VUE_APP_API_ENDPOINT,
      question: "Who are our 5 best customers?",
      msg: 'Hello!',
      data: [{"":""},{"":""},{"":""},{"":""},{"":""}],
      sql_query: '',
      do_setup: false
    };
  },
  methods: {
    checkSetup() {
       axios.get(this.api_endpoint + '/setup').then((res) => this.do_setup = res.data.needsSetup)
    },
    getMessage() {
      const path = this.api_endpoint + '/question' // e.g. https://acolyte-api.herokuapp.com/api/question';
      const body = {
        question: this.question
      }
      axios.post(path, body)
        .then((res) => {
          this.msg = res.data;
          this.data = res.data.res;
          this.sql_query = res.data.query;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },

    submit() {
      this.data = [{"":"loading..."}];
      this.sql_query = 'loading...'
      this.getMessage();
      //this.loading = false;
    }
  },

  components: {
    DataTable,
    SetupModal
  },

  beforeMount() {
    this.checkSetup();
  }
};
</script>