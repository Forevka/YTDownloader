<template>
  <div class="main-div">
    <section>
      <b-field label="Link">
        <b-input class="yt-link-input" v-model="yt_link"></b-input>
      </b-field>
      <b-button type="is-success" v-on:click="userSumbit">Submit</b-button>

      <b-field>
        <b-radio-button
          v-for="q in qualityList"
          :key="q.id.value"
          v-model="radioButton"
          :native-value="q.name"
          type="is-success"
        >
          <span>{{q.name}}</span>
        </b-radio-button>
      </b-field>
    </section>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";
import { FilesApi } from "@/services/FilesApi";
import { FileQuality } from "@/enums/QualityEnum";
import { IFile } from "../models/IFile";
import { Dictionary } from "vue-router/types/router";
import { IQuality } from "../models/IQuality";

@Component
export default class YouTubeLinkUI extends Vue {
  @Prop() private msg!: string;
  private yt_link: string = "";
  private radioButton: string = "Default";
  private file!: IFile;
  private fileQuality: FileQuality = FileQuality.Good;
  private qualityList: IQuality[] = [];

  constructor() {
    super();
  }

  async mounted(): Promise<void> {
    this.qualityList = await FilesApi.getAvailableQuality();
    this.qualityList.forEach(x => console.log(x.id));
  }

  userSumbit(): void {
    console.log(this.yt_link);
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.main-div {
  display: inline-flex;
}

.yt-link-input {
  padding-left: 25%;
  padding-right: 25%;
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
