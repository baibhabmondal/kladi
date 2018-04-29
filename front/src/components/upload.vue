<template>

  <v-container grid-list-lg>

    <v-layout row wrap>
      <v-flex lg3 v-for="(heading,i) in headings" :key="i" mt-4>
        <v-card class="white--text" v-bind:style="{ backgroundImage: 'url(' + heading.image1 + ')' }" style="opacity:0.8;background-size:cover;height:100%;">
          <v-container fluid grid-list-lg class="body">
            <v-layout row>
              <v-flex xs12>
                <div style="padding:30px 0px">

                  <router-link to="/upload" class="headline1">{{ heading.title }}</router-link>
                  <div style="padding:30px 20px">{{ heading.description }}</div>
                </div>
              </v-flex>
            </v-layout>
          </v-container>
        </v-card>

      </v-flex>

    </v-layout>

    <v-layout row wrap>
      <v-flex xs3 v-for="(heading,i) in headings" :key="i" mt-4>
        <v-card class="white--text" v-bind:style="{ backgroundImage: 'url(' + heading.image1 + ')' }" style="opacity:0.8;background-size:cover;height:100%;">
          <v-container fluid grid-list-lg class="body">
            <v-layout row>
              <v-flex xs12>
                <div style="padding:30px 0px">

                  <router-link to="/upload" class="headline1">{{ heading.title }}</router-link>
                  <div style="padding:30px 20px">{{ heading.description }}</div>
                </div>
              </v-flex>
            </v-layout>
          </v-container>
        </v-card>

      </v-flex>

    </v-layout>

    <v-layout row wrap>
      <v-flex xs3 v-for="(heading,i) in headings" :key="i" mt-4>
        <v-card class="white--text" v-bind:style="{ backgroundImage: 'url(' + heading.image1 + ')' }" style="opacity:0.8;background-size:cover;height:100%;">
          <v-container fluid grid-list-lg class="body">
            <v-layout row>
              <v-flex xs12>
                <div style="padding:30px 0px">

                  <router-link to="/upload" class="headline1">{{ heading.title }}</router-link>
                  <div style="padding:30px 20px">{{ heading.description }}</div>
                </div>
              </v-flex>
            </v-layout>
          </v-container>
        </v-card>

      </v-flex>

    </v-layout>

  </v-container>


</template>

<script>
  import axios from 'axios'
  export default {
    data() {
      return {
        headings: [
          {
            description:'This Specialization builds on the success of the Python for Everybody course and will introduce fundamental programming concepts.',
            title: 'PHYSICS',
            url: ''
          },
          {
             description: 'This Specialization builds on the success of the Python for Everybody course and will introduce fundamental programming concepts.',
            title: 'BIOLOGY',
            url: ''
          },
          {
             description: 'This Specialization builds on the success of the Python for Everybody course and will introduce fundamental programming concepts.',
            title: 'CHEMISTRY',
            url: ''
          },
          {
             description: 'This Specialization builds on the success of the Python for Everybody course and will introduce fundamental programming concepts.',
            title: 'COMPUTER',
            url: ''
          }
        ]
      }
    },
    created() {
      axios.get(`http://jsonplaceholder.typicode.com/posts`)
        .then(response => {
          this.headings.title = response.data;
          this.headings.url = response.data;
          console.log(this.headings.title)

        })
        .catch(e => {
          this.errors.push(e)
        })
    }
  }

</script>
<style scoped>
  a {
    text-decoration: none;
    color: white;
  }

  .white--text {
    background-color: #006064;
    font-family: 'Source Sans Pro', sans-serif;
    border-radius: 2px;
    width: 95%;
  }

  .body:hover {
    background: blue;
    opacity: 0.7
  }

  .headline1 {
    font-size: 40px;
  
  }
</style>