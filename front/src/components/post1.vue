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
                description: '',
                files: ''
            }
        },
        methods: {

        }
    }

</script>
<style scoped>
    .outer {
        border: 1px solid black;
    }

    h2,
    h3 {
        padding: 20px 0 20px 0;
    }
</style>