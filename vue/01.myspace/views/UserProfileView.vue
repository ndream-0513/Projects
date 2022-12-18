<template>
    <ContentBase>
      <div class="row">
        <div class="col-3">
          <UserProfileInfo @follow="follow" @unfollow="unfollow" :user="user"></UserProfileInfo>
        </div>
        <div class="col-9">
          帖子信息
        </div>
      </div>
    </ContentBase>
</template>
  
<script>
import ContentBase from '@/components/ContentBase.vue';
import UserProfileInfo from '@/components/UserProfileInfo.vue';
import { reactive } from 'vue';

export default {
  name: 'UserProfileView',
  components: {
    ContentBase,
    UserProfileInfo,
  },

  setup() {
    const user = reactive({
      id: 1,
      userName: 'ndream',
      lastName: 'n',
      firstName: 'dream',
      followerCount: 0,
      is_followed: false,
    });

    const follow = () => {
      if (user.is_followed) return;
      user.is_followed = true;
      user.followerCount ++;
    };
    const unfollow = () => {
      if (!user.is_followed) return;
      user.is_followed = false;
      user.followerCount --;
    };

    return {
      user: user,
      follow,
      unfollow,
    }
  }

}
</script>
  