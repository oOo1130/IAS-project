<template>
  <small-card title="2D Deconvolution">
    <custom-button icon="play-circle" label="2D-Go" @click="select1" />
    <custom-button icon="cog" label="Set" @click="select2" />
  </small-card>
</template>

<script>
import SmallCard from "../../../custom/SmallCard";
import CustomButton from "../../../custom/CustomButton";

export default {
  name: "Dec2D",

  components: {
    SmallCard,
    CustomButton
  },

  data: () => ({}),

  methods: {
    select1: function() {
        var formData = new FormData();
        var image_name = this.$store.state.image.imageUri
        formData.append("files_name", image_name);
        this.$store.dispatch("image/convol2D", formData); 
    },
    select2: function() {
      console.log("Select-2");
    }
  }
};
</script>
