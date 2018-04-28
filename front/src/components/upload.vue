<template>
  <div>
    <v-container text-xs-left>
      <v-layout row wrap>
        <v-flex xs3 v-for="(heading,i) in headings" :key="i" mt-4>
          <v-card class="white--text">
            <v-container fluid grid-list-lg>
              <v-layout row>
                <v-flex xs12>
                  <div style="padding:30px">

                    <router-link to="/post1" class="headline"> post</router-link>
                    <div></div>
                  </div>
                </v-flex>
              </v-layout>
            </v-container>
          </v-card>

        </v-flex>

      </v-layout>
      </v-container>
      
    </v-container>
  </div>
</template>
<script>
  export default {
    name: 'upload',
    data() {
      return {
        tags:'PHYSICS',
        description:'',
        files:''
      }
    },
    methods: {
     
    }
  }

</script>
<style scoped>
  .outer{
    border:1px solid black;
  }
  h2,h3{
    padding:20px 0 20px 0;
  }
</style>