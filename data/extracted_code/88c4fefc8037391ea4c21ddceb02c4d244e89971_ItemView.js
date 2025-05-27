// Internal imports
import styles from "./ItemView.styles";
import ChooseAmount from '../ChooseAmount/ChooseAmount';

// Constants
const DEFAULT_UNIT = "יח'";
const WEIGHTED_UNITS = ["100 גרם", '100 מ"ל'];

// Assets
const delete_image = require("../../assets/images/delete.png");

/**
 * ItemView Component
 * Displays an item card with name, amount selector, and delete button
 *
 * @param {Object} item - The item to display
 * @param {Function} handleDelete - Callback for delete action
 * @param {Function} addAmount - Callback for amount changes
 */
const ItemView = ({ item, handleDelete, addAmount }) => {
    // Unit calculations if type is addItem

    const unit = item.measurementUnit.replace('ק"ג', "100 גרם").replace("ליטר", '100 מ"ל');
    const weighted = item.weighted && WEIGHTED_UNITS.includes(unit);

    const finalUnit = weighted ? unit.replace("100 ", "") : DEFAULT_UNIT;
    const unitCalcResults = {
        step: weighted ? 100 : 1,
        maxAmount: finalUnit == "יח'" ? 10000 : 100000,
        finalUnit: finalUnit,
        weighted: weighted,
    };


    return (
        <View style={[styles.card, styles.shadow]}>
            {/* Item name */}
            <Text
                style={[styles.right, styles.text]}
                numberOfLines={2}
                adjustsFontSizeToFit={true}
            >
                {item.name}
            </Text>

            {/* Amount selector and delete button container */}
            <View style={styles.alignLeft}>
                {/* Amount selector */}
                <ChooseAmount
                    unitCalcResults={unitCalcResults}
                    onAmountChange={(amount) => addAmount(amount)}
                    item={item}
                    displayReset={false}
                    small={true}
                />

                {/* Delete button */}
                <TouchableOpacity onPress={handleDelete} activeOpacity={1}>
                    <Image style={styles.delete} source={delete_image} />
                </TouchableOpacity>
            </View>
        </View>
    );
};

export default ItemView;