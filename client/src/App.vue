<template>
  <Question/>
</template>

<script>
import Question from './components/Question.vue'

export default {
  name: 'App',
  components: {
    Question
  }
}
</script>

<style>
  #title a {
    text-decoration: underline;
    text-decoration-color: var(--bs-yellow);
  }

  body {
    background-color: var(--bs-light);
  }

  .container {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: var(--bs-dark);
    margin: 0px auto 20px auto;
    background-color: lavender;
    border-radius: 5px;
    padding: 10px 20px 20px 20px;
    border-color: white;
    border-width: 1px;
  }

  .container a{
    text-decoration: solid;
    background-color: darkslateblue;
    padding: 3px;
    border-radius: 3px;
    color: whitesmoke;
  }

  .container a:hover {
    background-color: var(--bs-yellow);
  }

  #header {
    font-size: 2em;
  }

  #question {
    border: 2px solid var(--bs-yellow);
    padding: 5px;
    border-radius: 5px;
    background-color: whitesmoke;
    color: var(--bs-gray-700)
  }
  #submit {
    border: 2px solid var(--bs-yellow);
    padding: 5px;
    border-radius: 5px;
    background-color: darkslateblue;
    color: whitesmoke;
  }

  @media only screen 
    and (max-device-width: 600px) {
    #submit {
      width: 100%;
      margin-top: 10px;
    }
    #question {
      width: 100%;
    }
    .container {
      width: 90%
    }
  }

  @media only screen 
    and (min-device-width: 600px) {
    #submit {
      width: 20%;
      margin-left: 10px;
    }
    #question {
      width: 75%;
    }
    .container {
      width: 66%;
    }
  }

  #submit:hover {
    background-color :var(--bs-yellow);
  }
  #submit:active {
    border-color: grey;
  }
  .data-table {
    padding-top: 10px;
  }

  #title {
    font-size: 3em;
    background-color: aliceblue;
    padding: 30px;
    margin-bottom: 20px;
    display: block;
    border-color: white;
    border-width: 0 0 1px 0;
  }

  #title-container {
    width: 80%;
  }

  #question-form {
    padding: 20px;
  }

  code {
    background-color: white;
    display: block;
    border-radius: 5px;
    padding: 10px;
  }

  input:focus,
  select:focus,
  textarea:focus,
  button:focus {
    outline: none;
  }

  #setup-container {
    width: 100%;
    height: 100%;
    left: 0px;
    top: 0px;
    position: fixed;
    z-index: 10000;
    background-color: rgba(0,0,0,0.5)
  }

  #setup-modal {
    width: 80%;
    height: 80%;
    background-color: var(--bs-light);
    margin: auto;
    display: block;
    border-radius: 3px;
    border-color: white;
    border-width: 1px;
    opacity: 1;
    overflow: auto;
    position: absolute;
    top: 0; left: 0; bottom: 0; right: 0;
    padding: 20px;
  }

  @import './assets/style.css';
  @import '../node_modules/bootstrap/dist/css/bootstrap.min.css';
</style>
