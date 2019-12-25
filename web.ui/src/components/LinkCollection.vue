<template>
  <div class="collection-content">
    <transition-group name="list" tag="ul">
      <li v-for="i in filtered_cards()" :key="i.id">
        <YouTubeLinkUI :id="i.id" v-on:delete_card="delete_card"/>
      </li>
    </transition-group>
    <b-button type="is-success" @click="add_card()">Add one link</b-button>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";
import YouTubeLinkUI from "./YouTubeLinkUI.vue";

@Component({
  components: { YouTubeLinkUI }
})
export default class LinkCollection extends Vue {
  private cards: object[] = [];
  private ids: number = 0;
  constructor() {
    super();
  }

  async mounted(): Promise<void> {
    this.cards.push({id: this.ids})
  }

  add_card(): void {
    this.ids += 1;
    this.cards.push({id: this.ids})
  }

  delete_card(card_id: number): void {
    console.log(card_id)
    let index = this.cards.indexOf({id: card_id})
    if (index)
    {
      this.cards.splice(index, 1);
    }
  }

  filtered_cards(): object[] {
    return this.cards
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.list-item {
  display: inline-block;
  margin-right: 10px;
}
.list-enter-active, .list-leave-active {
  transition: all 1s;
}
.list-enter, .list-leave-to /* .list-leave-active до версии 2.1.8 */ {
  opacity: 0;
  transform: translateY(30px);
}
</style>
