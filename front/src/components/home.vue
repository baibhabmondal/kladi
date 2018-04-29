<template>

      <v-container   grid-list-lg>
      
      <v-layout row wrap >
          <v-flex lg3 v-for="(heading,i) in headings" :key="i" mt-4 >
            <v-card class="white--text" v-bind:style="{ backgroundImage: 'url(' + heading.image1 + ')' }" style="opacity:0.8;background-size:cover;height:100%;">
              <v-container fluid grid-list-lg class="body">
                <v-layout row>
                  <v-flex xs12>
                    <div style="padding:30px;">

                      <a :href="heading.url" class="headline1">{{ heading.title }}</a>
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
              <v-container fluid grid-list-lg  class="body">
                <v-layout row>
                  <v-flex xs12>
                    <div style="padding:30px;">
                      
                      <a href="heading.url" class="headline1">{{ heading.title }}</a>
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
            <v-container fluid grid-list-lg  class="body">
              <v-layout row>
                <v-flex xs12>
                  <div style="padding:30px;">

                    <a  href="heading[i].url" class="headline1">{{ heading.title }}</a>
                    <div>{{ heading.description }}</div>
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
        errors: [], 
  headings:[
       {
        image1:'http://bfsi.eletsonline.com/wp-content/uploads/2018/02/Technology-based-lending.jpg',
         title: '',
         url:'http://localhost:6666/upload'
       },
       {
         image1:'https://www.feedsyndicate.com/wp-content/uploads/SportsNews.jpg',
         title: '',
        url: "http://localhost:7777/upload"
       },
      {
        image1:'http://bfsi.eletsonline.com/wp-content/uploads/2018/02/Technology-based-lending.jpg',
         title: '',
         url:''
       },
       {
         image1:'https://www.feedsyndicate.com/wp-content/uploads/SportsNews.jpg',
         title: '',
        url: ''
       }

             ]
      }
    },
   created(){
     var that = this
      axios.get(`http://localhost:5000/api/nodes/links`)
      .then(response=>{
      //  this.headings.title=response.data;
      console.log(typeof(response.data))
     var array = response.data.replace("'", "").substr(1).slice(0,-1).replace("'", "").split(",")
     console.log(array)
     for(var i=0;i<array.length;i++){
       that.headings[i].title=array[i]
     }
            })
    ,
          axios.get(`http://localhost:5000/api/nodes/values`)
      .then(response=>{
      //  this.headings.title=response.data;
      for(let i in response){
        that.headings[i].url=response[i]
      }
    //  var array = response.data.replace("'", "").substr(1).slice(0,-1).replace("'", "").split(",")
    //  console.log(array)
    //  for(var i=0;i<array.length;i++){
      //  that.headings[i].title=array[i]
    //  }
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
  background-color:rgb(43, 174, 179);
 font-family: 'Source Sans Pro', sans-serif;
  border-radius:7px;
  width:95%;
}
.body:hover{
  background:green;
  opacity:0.7
}
.headline1{
  font-size:40px;

}

  
</style>

