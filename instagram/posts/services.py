# django imports
from django.db import transaction

# app imports
from posts.models import Post, Reaction

class PostService:
    def create(self, user_id, content):
        try:
            post = Post.objects.create(
                user_id = user_id,
                content = content  
            )
            return post
        except Exception as e:
            print(f"Error is creating post: {e}")
            
    def modify(self, post_id, content):
        try:
            post = Post.objects.get(pk = post_id)
            post.content = content
            post.save()
            return post
        except Exception as e:
            print(f"Error is modifying post: {e}")

    def like(self, post_id, user_id):
        try:
            post = Post.objects.get(pk = post_id)
            qs = Reaction.objects.filter(
                user_id = user_id,
                post_id = post_id,
            )
            if qs.count() > 0:
                user_reaction = qs.first()
                if user_reaction.operation == 0:
                    return f"User {user_id} has already liked the post."
                else:
                    with transaction.atomic():
                        # change to like
                        user_reaction.operation = 0
                        user_reaction.save()
                        # increment like
                        # decrease dislike
                        post.likes = post.likes + 1
                        post.dislikes = post.dislikes - 1
                        post.save()
                    return f"User {user_id} has liked the post."
            else:
                # no reaction is present
                with transaction.atomic():
                    Reaction.objects.create(
                        user_id = user_id,
                        post_id = post_id,
                        operation = 0
                    )
                    post.likes = post.likes + 1
                    post.save()
                return f"User {user_id} has liked the post."
        except Exception as e:
            print(f"error in liking the post: {e}")

    def dislike(self, post_id, user_id):
        try:
            post = Post.objects.get(pk = post_id)
            qs = Reaction.objects.filter(
                user_id = user_id,
                post_id = post_id,
            )
            if qs.count() > 0:
                user_reaction = qs.first()
                if user_reaction.operation == 1:
                    return f"User {user_id} has already disliked the post."
                else:
                    with transaction.atomic():
                        # change to like
                        user_reaction.operation = 1
                        user_reaction.save()
                        # decrement like
                        # increment dislike
                        post.likes = post.likes - 1
                        post.dislikes = post.dislikes + 1
                        post.save()
                    return f"User {user_id} has disliked the post."
            else:
                # no reaction is present
                with transaction.atomic():
                    Reaction.objects.create(
                        user_id = user_id,
                        post_id = post_id,
                        operation = 0
                    )
                    post.dislikes = post.dislikes + 1
                    post.save()
                return f"User {user_id} has disliked the post."
        except Exception as e:
            print(f"error in disliking the post: {e}")
