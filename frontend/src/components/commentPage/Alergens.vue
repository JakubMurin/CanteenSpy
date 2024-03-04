<template>
    <div class="alergens-box">
        <div @click="toggleAlergens" class="toggle-alergens">
            <h3>Alergény</h3>
            <img v-if="!isOpen" src="@/assets/images/caret-down-fill.svg" alt="arrow">
            <img v-else src="@/assets/images/caret-up-fill.svg" alt="arrow">
        </div>
        <div id="alergens-content">
            <ol>
                <li>Obilniny obsahujúce lepok (t.j. pšenica, raž, jačmeň, ovos, špalda, kamut alebo ich hybridné odrody).</li>
                <li>Kôrovce a výrobky z nich.</li>
                <li>Vajcia a výrobky z nich.</li>
                <li>Ryby a výrobky z nich.</li>
                <li>Arašidy a výrobky z nich.</li>
                <li>Sójové zrná a výrobky z nich.</li>
                <li>Mlieko a výrobky z neho.</li>
                <li>Orechy, ktorými sú mandle, lieskové orechy, vlašské orechy, kešu, pekanové orechy, para orechy, pistácie, makadamové orechy a queenslandské orechy a výrobky z nich.</li>
                <li>Zeler a výrobky z neho.</li>
                <li>Horčica a výrobky z nej.</li>
                <li>Sezamové semená a výrobky z nich.</li>
                <li>Oxid siričitý a siričitany v koncentráciách vyšších ako 10 mg/kg alebo 10 mg/l. /konzervanty/</li>
                <li>Vlčí bob a výrobky z neho.</li>
                <li>Mäkkýše a výrobky z nich.</li>
            </ol>
        </div>
    </div>
</template>

<script>
export default {
  name: 'Alergens',
  data() {
    return {
        show: false,
        isOpen: false
    }
  },
  methods: {
    toggleAlergens() {
        if (this.isOpen) {
            this.isOpen = false;
            document.getElementById('alergens-content').style.display = "none";
        } else {
            this.isOpen = true;
            document.getElementById('alergens-content').style.display = "block";
        }
    }
  },
  mounted() {
    if (document.getElementById('alergens-content').style.display == "block") {
       this.isOpen = true;
    } else {
        this.isOpen = false;
    }
  }
}
</script>
