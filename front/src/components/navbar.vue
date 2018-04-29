<template>

  <div>
    <v-toolbar class="toolbar">
<img src="https://thelogo.shop/wp-content/uploads/2016/12/02-Letter-K.png">
      <v-toolbar-title class="title">KLADI</v-toolbar-title>
        <v-flex lg4 offset-lg3 text-xs-left>
          <div class="box">
            <div class="container-1">
              <span class="icon"><i class="fa fa-search"></i></span>
              <input type="search" id="search" placeholder="Search..." />
            </div>
          
          </div>

        </v-flex>
      <v-spacer></v-spacer>
      <router-link to="/post">
      <v-btn fab small depressed outline dark color="teal darken-4">
       <i class="material-icons" dark style="font-size:28px;"> add</i>
      </v-btn>
      </router-link>
    </v-toolbar>
  
  </div>
</template>
<script>

</script>
<style scoped>
  img{
    height:40px;
    width:40px;
  }
 .toolbar{
   background:#CFEDFC;
 font-family: 'Vollkorn', serif;
  
 }
 a{
   text-decoration:none;
   color:#2C2828
 }
 .container-1 input#search:hover, .container-1 input#search:focus, .container-1 input#search{
   border:2px solid #CAC2C2;
   background: white;
    opacity:0.6;
    border-radius:8px;
    width:80%;
    height:35px;
    padding:0px 15px;
  }
  .icon{
    color:#7A7575;
    padding-right:5px
  }
  i:hover{
    color:blue
  }
  i:focus{
    color:blue
  }



  </style>