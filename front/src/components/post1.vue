<template>
  <div>
    <v-container fluid grid-list-lg text-xs-left>
      <v-layout row wrap>
        <v-flex lg8 offset-lg2>
           <v-container class="outer">
            <v-layout row wrap>

                <v-flex>
                    <h2>{{title}}</h2>
                </v-flex>
            </v-layout>
            <v-layout row wrap>
                <v-flex lg4>
                <img src="https://discourse-cdn-sjc1.com/business5/uploads/safenetwork/229/640699c8fee8c788.png">
                </v-flex>
            </v-layout>
         
          
           
            <v-layout row wrap >
              <v-flex>
                {{description}}
              </v-flex>
            </v-layout>
          </v-container>
        </v-flex>
    
      </v-layout>
      
      <hr>
      <v-layout style="margin-left:70px;margin-top:10px" row wrap>
          <h1>Other Posts</h1>
      </v-layout>
      
        <v-layout row wrap style="margin-left:70px;margin-right:70px">
            <v-flex xs3 v-for="(heading,i) in headings" :key="i" mt-4>
                <v-card class="white--text" v-bind:style="{ backgroundImage: 'url(' + heading.image1 + ')' }" style="opacity:0.8;background-size:cover;height:100%;">
                    <v-container fluid grid-list-lg class="body">
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
  </div>
</template>
<script>
  export default {
    name: 'upload',
    data() {
      return {
        title: 'Decentralisation for beginners',
        description: 'This specialization builds on the success of the Python for Everybody course and will introduce fundamental programming concepts.',
        files: '',
         headings: [
                {
                    image1: 'http://bfsi.eletsonline.com/wp-content/uploads/2018/02/Technology-based-lending.jpg',
                    title: 'SCIENCE',
                    url: ''
                },
                {
                    image1: 'https://www.feedsyndicate.com/wp-content/uploads/SportsNews.jpg',
                    title: 'POLITICS',
                    url: ''
                },
                {
                    image1: 'https://beta.techcrunch.com/wp-content/uploads/2017/10/explore-feed_preview.jpeg?w=680',
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
    created() {
      axios.get(`http://jsonplaceholder.typicode.com/posts`)
        .then(response => {
          this.tags = response.data;
          this.description = response.data;
          this.files = response.data;
          console.log(this.headings.title)

        })
        .catch(e => {
          this.errors.push(e)
        })
    }
  }

</script>
<style scoped>
  .outer {
  
    border-radius: 10px;
    font-family: 'Source Sans Pro', sans-serif;
    font-size: 18px;
    background:#E3F2FB;
    padding:20px 40px 30px 40px;
  }
img{
    margin-bottom:30px;
  margin-left:40px;
}
  h2,
  h3 {
    padding: 20px 0 20px 0px
  }

  hr {
    margin-top: 3%;
  }
  h1{
      margin-top:20px;
      font-size:20px;
      margin-left:15px;
  }
  a{
  text-decoration:none;
  color:white;
}
.headline1{
  font-size:40px;

}
.white--text{
  background-color:rgb(43, 174, 179);
 font-family: 'Source Sans Pro', sans-serif;
  border-radius:7px;
  width:95%;
}

</style>
