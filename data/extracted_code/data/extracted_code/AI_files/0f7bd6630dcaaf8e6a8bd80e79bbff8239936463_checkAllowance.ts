/** 
 * Use environment variables to provide arguments 
 * export contractAddress=""
 * export spender=""
 * export amount=""
 * Run the script with hardhat run 
 * npx hardhat run scripts/approveTokens.ts --network sepolia 
 */
import { ethers } from "hardhat";

async function approveTokens(contractAddress: string, spender: string, amount: string) {
  const GLDToken = await ethers.getContractFactory("GLDToken");
  const token = GLDToken.attach(contractAddress);

  const tx = await token.approve(spender, ethers.utils.parseUnits(amount, 18));
  console.log(`Approved ${amount} GLD for ${spender}. Transaction hash: ${tx.hash}`);
}

const contractAddress = process.env.contractAddress as string;
const spender = process.env.spender as string;
const amount = process.env.amount as string;

approveTokens(contractAddress, spender, amount)
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });