const SchemaTag = builder.objectRef<
  Omit<TagObject, "name"> & { name?: string; slug?: string }
>("SchemaTag");

SchemaTag.implement({
  fields: (t) => ({
    name: t.exposeString("name", { nullable: true }),
    slug: t.exposeString("slug", { nullable: true }),
    isUntagged: t.field({ type: "Boolean", resolve: (parent) => !parent.name }),
    description: t.exposeString("description", { nullable: true }),
    operations: t.field({
      type: [OperationItem],
      resolve: (parent, _args, ctx) => {
        const rootTags = ctx.tags.map((tag) => tag.name);

        return ctx.operations
          .filter((item) =>
            parent.name
              ? item.tags?.includes(parent.name)
              : item.tags?.length === 0 ||
                // If none of the tags are present in the root tags, then show them here
                item.tags?.every((tag) => !rootTags.includes(tag)),
          )
          .map((item) => ({ ...item, parentTag: parent.name }));
      },