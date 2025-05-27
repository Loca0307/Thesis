	ID            int64  `db:"id" json:"id,omitempty"`                           // Unique user id
	Firstname     string `db:"firstname" json:"first_name,omitempty"`            // Firstname
	Lastname      string `db:"lastname" json:"last_name,omitempty"`              // Lastname
	Email         string `db:"email" json:"email,omitempty"`                     // Email
	Username      string `db:"username" json:"username,omitempty"`               // Unique username
	FriendsCount  int    `db:"friends_count" json:"friends_count,omitempty"`     // Number of friends
	ProfilePicURL string `db:"profile_pic_url" json:"profile_pic_url,omitempty"` // Profile picture
	PostsCount    int    `db:"posts_count" json:"posts_count,omitempty"`         // Number of posts
	CommentsCount int    `db:"comments_count" json:"comments_count,omitempty"`   // Number of comments
	LikesCount    int    `db:"likes_count" json:"likes_count,omitempty"`         // Number of likes