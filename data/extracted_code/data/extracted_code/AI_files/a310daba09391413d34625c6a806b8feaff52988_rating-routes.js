const router = require('express').Router();
const { Rating } = require('../../models');

// these aren't definite routes, just a starting point based off what I think we need.
// route to get all ratings
router.get("/", async (req, res) => {
  try {
    const ratingData = await Rating.findAll();
    res.status(200).json(ratingData);
  } catch (err) {
    res.status(500).json(err);
  }
});

// route to get one rating
router.get("/:id", async (req, res) => {
  try {
    const ratingData = await Rating.findByPk(req.params.id);
    if (!ratingData) {
      res.status(404).json({ message: "No rating found with this id!" });
      return;
    }
    res.status(200).json(ratingData);
  } catch (err) {
    res.status(500).json(err);
  }
});

// router to get all ratings by user
router.get("/user/:user_id", async (req, res) => {
  try {
    const ratingData = await Rating.findAll({ where: { user_id: req.params.user_id } });
    if (!ratingData) {
      res.status(404).json({ message: "No ratings found with this user!" });
      return;
    }
    res.status(200).json(ratingData);
  } catch (err) {
    res.status(500).json(err);
  }
});

// route to get one rating by user
router.get("/user/:user_id/:id", async (req, res) => {
  try {
    const ratingData = await Rating.findOne({ where: { user_id: req.params.user_id, id: req.params.id } });
    if (!ratingData) {
      res.status(404).json({ message: "No rating found with this user!" });
      return;
    }
    res.status(200).json(ratingData);
  } catch (err) {
    res.status(500).json(err);
  }
});


// copilot mumbo jumbo, don't know if we need, but can be used as a reference for the future
// route to get average rating for a song
router.get("/average/:music_id", async (req, res) => {
  try {
    const ratingData = await Rating.findAll({ where: { music_id: req.params.music_id } });
    if (!ratingData) {
      res.status(404).json({ message: "No ratings found for this song!" });
      return;
    }
    let total = 0;
    for (let i = 0; i < ratingData.length; i++) {
      total += ratingData[i].rating;
    }
    const average = total / ratingData.length;
    res.status(200).json(average);
  } catch (err) {
    res.status(500).json(err);
  }
});

module.exports = router;