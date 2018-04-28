<template>
  <div>
    <v-app>
      <h1>INDIVIDUAL POST PAGE</h1>
      <v-container>
        <v-layout row wrap>
          <!-- <v-flex offset-lg3 lg3>
    <v-btn raised class="button" style="background:#666; color: white; " @click="onPickFile">UPLOAD</v-btn>
    </v-flex> -->
    <v-flex offset-lg3 lg6>
   <div >
   <v-btn raised class="button" style="background:#666; color: white; " @click="onPickFile">UPLOAD</v-btn>
    <input type="file" id="attachments" style="display: none;" ref="file" class="input-file" @change="uploadFieldChange($event)">
   
    </div>
  </v-flex>

    </v-layout>
    <v-layout row wrap>
      <v-flex offset-lg3 lg6>
        <div v-if="flag">
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
        <v-text-field  v-model="des" label="DESCRIPTION" multi-line></v-text-field>
      
       </v-flex>
    </v-layout>
    <v-layout row wrap>
       <v-flex offset-lg3 lg6>
        <v-select :items="items" no-data-text="No nodes" hint="Tags (max 3)" persistent-hint ref="tags" v-model="chips" autocomplete chips clearable multiple deletable-chips hide-selected>TAGS</v-select>
      
       </v-flex>
    </v-layout>
    <v-layout row wrap>
      <v-flex offset-lg3 lg6>
      <v-btn raised class="button" style="background:#666; color: white;" @click="submit">SUBMIT</v-btn>
    </v-flex>
    </v-layout>
  </v-container>
  </v-app>
  </div>
</template>
<script>
  import axios from 'axios'
 
  export default {
   
    name: 'post',
    data () {
      return {
        caption: "",
        des: "",
        files: null,
        chips: "",
         
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

        console.log(this.chips)

        // console.log(this.caption)
        // console.log(this.des)
        // console.log(this.files)

        this.attachments = {
          files: this.files,
          
          des: this.des,
          tags: this.tags
        }

        let data = new FormData();
        // console.log(this.attachments)
            for (const key of Object.keys(this.attachments)) {
                // console.log(key, this.form[key])
                data.append(key, this.attachments[key]);
                // console.log(data)NPM RUN DEV;
              }
              console.log(data)

        //post request to icy's node on cloud 
        axios.post('http://jsonplaceholder.typicode.com/posts', data)
        .then(response => {
          console.log(response)
        })
        .catch()
          
      }

    },
  
  }

</script>

<style scoped>
   .button{
    width:80px;
    height:30px;
    margin-top:7%;
  
  }

  .dropbox {
    outline: 2px dashed grey; /* the dash box */
    outline-offset: -10px;
    background: lightcyan;
    color: dimgray;
    padding: 10px 10px;
    min-height: 200px; /* minimum height */
    position: relative;
    cursor: pointer;
  }
/* 
  .input-file {
    opacity: 0;
    width: 100%;
    height: 200px;
    position: absolute;
    cursor: pointer;
  } */

  .dropbox:hover {
    background: lightblue; /* when mouse over to the drop zone, change color */
  }

  .dropbox p {
    font-size: 1.2em;
    text-align: center;
    padding: 50px 0;
  }
</style>