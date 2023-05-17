const express = require("express");
const router = express.Router();

const {
  getUserById,
  getUser,
  updateUser,
  blockUser,
  unblockUser
} = require("../controllers/user");
const { isSignedIn, isAuthenticated, isAdmin } = require("../controllers/auth");

router.param("userId", getUserById);

router.get("/user/:userId", isSignedIn, isAuthenticated, getUser);
router.put("/user/:userId", isSignedIn, isAuthenticated, updateUser);

// Block And UnBlock a User
router.put("/user/block/:userId", isSignedIn, isAuthenticated, isAdmin, blockUser);
router.put("/user/unblock/:userId", isSignedIn, isAuthenticated, isAdmin, unblockUser);

// router.get(
//   "/orders/user/:userId",
//   isSignedIn,
//   isAuthenticated,
//   userPurchaseList
// );

module.exports = router;