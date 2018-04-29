<template>
<v-app>
      <v-container fluid grid-list-lg>
        <v-layout row wrap>
          <v-flex lg5 offset-lg4 text-xs-left>
            
           <div class="wrap">
   <div class="search">
      <input type="text" class="searchTerm" placeholder="What are you looking for?">
      <button type="submit" class="searchButton">
        <i class="fa fa-search"></i>
     </button>
   </div>
</div>
            
          </v-flex>
        </v-layout>
      <v-layout row wrap>
        <v-flex xs3 v-for="(heading,i) in headings" :key="i" mt-4>
          <v-card class="white--text"  v-bind:style="{ backgroundImage: 'url(' + heading.image1 + ')' }" style="opacity:0.8;background-size:cover;height:100%;">
            <v-container fluid grid-list-lg>
              <v-layout row>
                <v-flex xs12>
                  <div style="padding:30px">
                    
                    <router-link to="/upload" class="headline1">{{ heading.title }}</router-link>
                    <div>{{ heading.description }}</div>
                  </div>
                </v-flex>
              </v-layout>
            </v-container>
          </v-card>

        </v-flex>

      </v-layout>
        
        <v-layout row wrap >
          <v-flex xs3 v-for="(heading,i) in headings" :key="i" mt-4 >
            <v-card class="white--text"  v-bind:style="{ backgroundImage: 'url(' + heading.image1 + ')' }" style="opacity:0.8;background-size:cover;height:100%;">
              <v-container fluid grid-list-lg>
                <v-layout row>
                  <v-flex xs12>
                    <div style="padding:30px;">
                      
                      <router-link to="/upload" class="headline1">{{ heading.title }}</router-link>
                      <div>{{ heading.description }}</div>
                    </div>
                  </v-flex>
                </v-layout>
              </v-container>
            </v-card>

          </v-flex>

        </v-layout>
     
      <v-layout row wrap>
        <v-flex xs3 v-for="(heading,i) in headings" :key="i" mt-4>
          <v-card class="white--text"  v-bind:style="{ backgroundImage: 'url(' + heading.image1 + ')' }" style="opacity:0.8;background-size:cover;height:100%;">
            <v-container fluid grid-list-lg>
              <v-layout row>
                <v-flex xs12>
                  <div style="padding:30px;">

                    <router-link to="/upload" class="headline1">{{ heading.title }}</router-link>
                    <div>{{ heading.description }}</div>
                  </div>
                </v-flex>
              </v-layout>
            </v-container>
          </v-card>

        </v-flex>

      </v-layout>
        
      </v-container>
     
</v-app>
</template>

<script>
  import axios from 'axios'
  export default {
    data() {
      return {
        errors: [], 
  headings:[
       {
        image1:'http://bfsi.eletsonline.com/wp-content/uploads/2018/02/Technology-based-lending.jpg',
         title: 'SCIENCE',
         url:''
       },
       {
         image1:'https://www.feedsyndicate.com/wp-content/uploads/SportsNews.jpg',
         title: 'POLITICS',
        url: ''
       },
       {
        image1:'https://beta.techcrunch.com/wp-content/uploads/2017/10/explore-feed_preview.jpeg?w=680',
         title: 'SCIENCE',
          url: ''
       },
         {
            image1: 'http://firedove.tech/wp-content/uploads/2017/08/cropped-christopher-gower-291246.jpg',
            title: 'POLITICS  ',
            url: ''
          }
      ]
      }
    },
   created(){
      axios.get(`http://localhost:5000/api/nodes/links`)
      .then(response=>{
        this.headings.title=response.data;
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
a{
  text-decoration:none;
  color:white;
}
.white--text{
  background-color:#006064;
  font-family: 'Vollkorn', serif;
  border-radius:7px;
}
.headline1{
  font-size:40px;

}

.search{
  border:2px solid #595961;
  border-radius:25px;
  padding:10px;
  
}


.searchTerm {
  
  width: 95%;
  
}
</style>

