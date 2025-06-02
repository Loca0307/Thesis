import { db } from '.';
import { champions, items } from './schema';
import { eq, inArray } from 'drizzle-orm';

export async function insertMissingChampionsAndItems(ddChampions: DDChampion[], ddItems: DDItem[]) {
  await db.transaction(async (tx) => {
    // Fetch all existing champions and items in one go
    const existingChampions = await tx.select().from(champions);
    const existingItems = await tx.select().from(items);

    // Create a set of existing champion names and item IDs for quick lookup
    const existingChampionNames = new Set(existingChampions.map((champ) => champ.name));
    const existingItemIds = new Set(existingItems.map((item) => item.id));

    // Filter out the champions and items that already exist
    const newChampions = ddChampions.filter((ddChampion) => !existingChampionNames.has(ddChampion.name));
    const newItems = ddItems.filter((ddItem) => !existingItemIds.has(ddItem.id));

    // Insert new champions and items in bulk
    if (newChampions.length > 0) {
      await tx.insert(champions).values(
        newChampions.map((ddChampion) => ({
          name: ddChampion.name,
        }))
      );
      console.log(`Inserted champions: ${newChampions.map((c) => c.name).join(', ')}`);
    } else {
      console.log('No new champions to insert.');
    }

    if (newItems.length > 0) {
      await tx.insert(items).values(
        newItems.map((ddItem) => ({
          id: ddItem.id,
          name: ddItem.name,
        }))
      );
      console.log(`Inserted items: ${newItems.map((i) => i.name).join(', ')}`);
    } else {
      console.log('No new items to insert.');
    }
  });
}