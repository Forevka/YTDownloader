<template>
  <div class="content">
    <section class="link-section">
      <b-field>
        <b-input
          class="yt-link-input"
          v-model="yt_link"
          placeholder="https://www.youtube.com/watch?v=yXmzBV9Ush0"
          :loading="yt_link_loading"
          @input="ytLinkInput"
        ></b-input>
      </b-field>
      <b-button class="delete-button" type="is-danger" icon-right="delete" @click="delete_self()">Delete</b-button>
      <h1>Select preffer quality</h1>
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
import { UrlTester } from "@/utilities/url_tester";

@Component
export default class YouTubeLinkUI extends Vue {
  @Prop() private msg!: string;
  public id: number = 0;
  private yt_link: string = "";
  private radioButton: string = "Default";
  private file!: IFile;
  private fileQuality: FileQuality = FileQuality.Good;
  private qualityList: IQuality[] = [];
  private yt_link_loading: boolean = false;

  private urlTester: UrlTester = new UrlTester();

  constructor() {
    super();
    console.log(this.id);
  }

  async mounted(): Promise<void> {
    //this.qualityList = await FilesApi.getAvailableQuality();
    //this.qualityList.forEach(x => console.log(x.id));
  }

  userSumbit(): void {
    console.log(this.yt_link);
    this.yt_link_loading = true;
  }

  ytLinkInput(value: string): void {
    console.log(value);
    console.log(this.urlTester.isValid(value));
  }

  delete_self(): void {
    this.$emit('delete_card', this.id)
    
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.link-section {
  //max-width: 50%;
  margin-left: 25%;
  margin-bottom: 25px;
  display: inherit;
  .yt-link-input {
    width: 80%;
  }
}

.content {
  display: flex;
  flex-direction: column;
}

.delete-button {
  position: relative;
  top: 0px;
  left: 20%;
}

h1 {
  font-size: 100%;
  font-weight: bold;
  display: flex;
  margin-bottom: 7px;
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
