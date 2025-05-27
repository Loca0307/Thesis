// module.exports.updateListing = async (req, res)=>{
//     let {id} = req.params;
//     let listing = await Listing.findByIdAndUpdate(id, {...req.body.listing});
//     if(typeof req.file != "undefined"){
//         let url = req.file.path;
//         let filename = req.file.filename;
//         listing.image = {url, filename};
//         await listing.save();
//     }
//     req.flash("success", "Listing Updated!");
//     res.redirect(`/listings/${id}`);
// };


// module.exports.updateListing = async (req, res) => {
//     try {
//         let { id } = req.params;
        
//         // Check if request body contains listing data
//         if (!req.body.listing) {
//             req.flash("error", "Invalid data provided!");
//             return res.redirect(`/listings/${id}/edit`);
//         }

//         // Update listing in DB
//         let listing = await Listing.findByIdAndUpdate(id, { ...req.body.listing }, { new: true });

//         // Handle file upload if a new image is provided
//         if (req.file) {
//             listing.image = {
//                 url: req.file.path,
//                 filename: req.file.filename
//             };
//             await listing.save();
//         }

//         req.flash("success", "Listing Updated!");
//         res.redirect(`/listings/${id}`);
//     } catch (error) {
//         console.error(error);
//         req.flash("error", "Something went wrong while updating the listing!");
//         res.redirect(`/listings/${id}/edit`);
//     }
// };


module.exports.updateListing = async (req, res) => {
    try {
        const { id } = req.params;
        const listing = await Listing.findById(id);
        if (!listing) return res.redirect("/listings");

        // If new images are uploaded, replace old ones in the database
        if (req.files?.length) {
            listing.images = req.files.map(({ path, filename }) => ({ url: path, filename }));
        }

        // Save updated listing