<template>
  <div class="main-div">
    <section>
      <b-field label="Name">
        <b-input value="Kevin Garvey"></b-input>
      </b-field>
    </section>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";
import { FilesApi } from "@/services/FilesApi";
import { IFile } from "../models/IFile";

@Component
export default class HelloWorld extends Vue {
  @Prop() private msg!: string;
  private file!: IFile;

  async mounted(): Promise<void> {
    this.file = await FilesApi.getFile("test");
    console.log(this.file);
    console.log(this.file.path);
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
