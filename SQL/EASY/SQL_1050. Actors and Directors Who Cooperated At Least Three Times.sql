select ad.actor_id, ad.director_id
from ActorDirector as ad
group by actor_id, director_id
having count(timestamp) >= 3