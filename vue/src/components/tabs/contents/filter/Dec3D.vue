<template>
  <small-card title="3D Deconvolution">
    <custom-button icon="play-circle" label="3D-Go" @click="select1" />
    <custom-button icon="cog" label="Setting" @click="settingDialog = true" />
    <!-- <open-setting-dialog v-model="settingDialog" /> -->
    <!-- <open-3D-setting-dialog v-model="settingDialog" /> -->
    <!-- <simple-dialog v-model="settingDialog" /> -->
  </small-card>
</template>

<script>
import SmallCard from "../../../custom/SmallCard";
import CustomButton from "../../../custom/CustomButton";
// import Open3DSettingDialog from "../file/Open3DSettingDialog";

export default {
  name: "Dec3D",

  components: {
    SmallCard,
    CustomButton,
    // Open3DSettingDialog
    // OpenFileDialog
    // SimpleDialog
  },

  data: () => ({}),

  methods: {
    select1: function() {
      console.log("Select-1");
    },
    select2: function() {
      console.log("Select-2");
    }
  }
};
</script>
