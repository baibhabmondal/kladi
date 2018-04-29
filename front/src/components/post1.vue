<template>
    <div>
        <v-container text-xs-left>
            <v-layout row wrap>
                <v-flex>
                    <h2>{{tags}}</h2>
                </v-flex>
            </v-layout>
            <v-container class="outer">
                <v-layout row wrap>

                    <v-flex>
                        <h3>Descriptions :</h3>
                    </v-flex>
                </v-layout>
                <v-layout row wrap>
                    <v-flex>
                        {{description}}
                    </v-flex>
                </v-layout>
                <hr>
                <v-layout row wrap>
                    <v-flex>
                        <h3> Videos/Pdfs Related :</h3>
                    </v-flex>
                </v-layout>
                <v-layout row wrap>
                    <v-flex>
                        {{files}}
                    </v-flex>

                </v-layout>
                <hr>
                <v-layout row wrap>
                    <v-flex>
                        <h3> LINKS :</h3>
                    </v-flex>
                </v-layout>
                <v-layout row wrap>
                    <v-flex>
                        {{links}}
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
                tags: 'PHYSICS',
                description: 'This Specialization builds on the success of the Python for Everybody course and will introduce fundamental programming concepts.',
                files: ''
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
        border: 2px solid #A39A9A;
        border-radius:5px;
        font-family: 'Source Sans Pro', sans-serif;
        font-size:18px;
    }

    h2,
    h3 {
        padding: 20px 0 20px 0px
        
    }
    hr{
        margin-top:3%;
    }
</style>