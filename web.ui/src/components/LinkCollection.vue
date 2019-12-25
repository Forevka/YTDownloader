<template>
  <div class="collection-content">
    <transition-group name="list" tag="ul">
      <li v-for="i in cards" :key="i.id">
        <YouTubeLinkUI @delete_card="delete_card(i.id)"/>
      </li>
    </transition-group>
    <b-button type="is-success" @click="add_card()">Add one link</b-button>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from "vue-property-decorator";
import YouTubeLinkUI from "./YouTubeLinkUI.vue";

class CardModel {
  id: number = 0;
}

@Component({
  components: { YouTubeLinkUI }
})
export default class LinkCollection extends Vue {
  private cards: CardModel[] = [];
  private ids: number = 0;
  constructor() {
    super();
  }

  async mounted(): Promise<void> {
    this.add_card()
  }

  add_card(): void {
    this.ids += 1;
    let card = new CardModel()
    card.id = this.ids
    this.cards.push(card)
  }

  delete_card(card_id: number): void {
    this.cards = this.cards.filter(function(value: CardModel, index: number, arr) {
      return value.id != card_id
    });
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
