<template>
  <div>
    <v-app>
      <v-layout row wrap>
      <v-flex offset-lg2 lg8>
      <v-container color="blue-grey lighten-4" mt-4 mb-4 class="box">
        <!-- <h1 class="heading">UPLOAD YOUR CONTENTS</h1> -->
        <v-layout row wrap>
          <!-- <v-flex offset-lg3 lg3>
    <v-btn raised class="button" style="background:#666; color: white; " @click="onPickFile">UPLOAD</v-btn>
    </v-flex> -->
    <v-flex offset-lg3 lg6>
   <div >
   <v-btn large raised color="teal darken-4"  class="button" style="background:#666; color: white; " @click="onPickFile">UPLOAD</v-btn>
    <input type="file" id="attachments" style="display: none;" ref="file" class="input-file" @change="uploadFieldChange($event)">
   
    </div>
  </v-flex>

    </v-layout>
    <v-layout row wrap>
      <v-flex offset-lg3 lg6>
        <div v-if="flag" class="remove">
          <span>{{ files.name + ' (' + Number((files.size / 1024 / 1024).toFixed(1)) + 'MB)'}}</span>
          <span @click="removeAttachment($event)"><button>Remove</button></span>
        </div>

      </v-flex>
    </v-layout>
    <!-- <v-layout row wrap>
       <v-flex offset-lg3 lg6>
          <v-text-field  v-model="caption" label="CAPTION" ></v-text-field>
       </v-flex>
    </v-layout> -->
    <v-layout row wrap>
       <v-flex offset-lg3 lg6>
        <v-text-field color="teal darken-4" box  v-model="des" label="DESCRIPTION" textarea></v-text-field>
      
       </v-flex>
    </v-layout>
    <v-layout row wrap>
       <v-flex offset-lg3 lg6>
        <v-select :items="items" color="teal darken-4" outline no-data-text="No nodes" hint="Tags (max 3)" persistent-hint ref="tags" v-model="chips" autocomplete chips clearable multiple deletable-chips hide-selected>TAGS</v-select>
      
       </v-flex>
    </v-layout>
    <v-radio-group  v-model="profileLink">
    <v-layout row wrap mt-3>
      <v-flex offset-lg3 lg1>
        <v-radio color="teal darken-4" value="anonym" class="radio" name="profile"></v-radio>
      </v-flex>
      <v-flex lg4>
        <p class="options">Upload Anonymously</p>
      </v-flex>
    </v-layout>
    <v-layout row wrap mt-2>
      <v-flex offset-lg3 lg1>
        <v-radio value="identifier" color="teal darken-4" class="radio" name="profile"></v-radio>
      </v-flex>
      <v-flex lg4>
        <p  class="options">Identifiers</p>
      </v-flex>
    </v-layout>
    </v-radio-group>
      <v-layout row wrap mt-2 v-if="profileLink=='identifier'">
        <v-flex offset-lg3 lg6>
        <v-text-field color="teal darken-4" box label="Profile Link">

        </v-text-field>
        </v-flex>
       
      </v-layout>
    <v-layout row wrap>
      <v-flex offset-lg3 lg6>
      <v-btn  raised large block color="teal darken-4" class="button" style="background:#666; color: white;" @click="submit">SUBMIT</v-btn>
    </v-flex>
    </v-layout>
  </v-container>
  </v-flex>
  </v-layout>
  </v-app>
  </div>
</template>
<script>
  import axios from 'axios'
 
  export default {
   
    name: 'post',
    data () {
      return {
        data: new FormData(),
        profile: true,
        profileLink: "anonym",
        caption: "",
        des: "",
        files: '',
        chips: [],
        errors: [],
        posts: null,
         
         tags: [],
         items: [
           'Sports',
           'Education',
           'Technology',
           'Politics',
           'Philosophy',
           'Science',
           'Religion'
           
         ],
          customFilter(item, queryText, itemText) {
              const hasValue = val => val != null ? val : ''
              const text = hasValue(item.name)
              const query = hasValue(queryText)
              return text.toString()
                .toLowerCase()
                .indexOf(query.toString().toLowerCase()) > -1
            },
         attachments: null,
        
         flag: 0
      
        //  content: null

      }
    },
    

    methods: {
      
      onPickFile() {
         
         this.$refs.file.click()

      },
      uploadFieldChange (e) {
        this.files = e.target.files[0];
        console.log(this.files)
        this.flag = 1;
      },
      removeAttachment(e) {
        console.log(e)
      this.files = null;
      this.$refs.file.value = null;
      this.flag = 0;
      
      },
      submit () {


        this.attachments = {
          files: this.files,
          profile: this.profileLink,
          
          des: this.des,
          tags: this.chips
        }
        console.log(this.attachments)

        
        // console.log(this.attachments)
            // for (const key of Object.keys(this.attachments)) {
                // console.log(key, this.form[key])
                data.append("myfile", this.files);
                data.append("des", this.attachments.des);
                data.append("tags",JSON.stringify(this.chips));

                // console.log(data)NPM RUN DEV;
              // }
              console.log(data)

        //post request to icy's node on cloud 
        axios.post('http://localhost:5000/api/upload', data,{headers:{'Content-Type':'multipart/form-data'}})
        .then(response => {
          console.log('response...')
          console.log(response)
        })
        .catch()
          
      }

    },
    created() {
        axios.get(`http://jsonplaceholder.typicode.com/posts`)
          .then(response => {
            // JSON responses are automatically parsed.
            this.posts = response.data;
            console.log(this.posts)
          })
          .catch(e => {
            this.errors.push(e)
          })
      }
    
  
  }

</script>

<style scoped>
   .button{
    /* width:80px;
    height:30px; */
    margin-top:2%;
    font-size: 28px;
  
  }
  .box{
    /* border: 2px solid #37474F; */
     border-radius: 10px;
     -webkit-box-shadow: -1px 1px 6px 0px rgba(0,77,64,1);
-moz-box-shadow: -1px 1px 6px 0px rgba(0,77,64,1);
box-shadow: -1px 1px 6px 0px rgba(0,77,64,1);
 background: #E3F2FD;

  }
  #app{
    background: #B2EBF2;
  }
  .heading{
    margin-top: 2%;
  }

  .remove{
    margin: 1%;
    font-size: 16px;
    /* font-family: 'helvetica'; */
  }
  .remove span:last-child{
    margin-left: 1%;
    font-size: 22px;
  }

  .options{
    font-size: 16px;
    font-weight: 600;

  }

  .radio{
    font-size: 22px;

  }

  
</style>