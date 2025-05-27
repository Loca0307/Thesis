			m, ok := tp.GetAlgorithm().GetMask().(*storepb.Algorithm_InnerOuterMask_)
			if ok && m.InnerOuterMask != nil {
				if m.InnerOuterMask.Type == storepb.Algorithm_InnerOuterMask_MASK_TYPE_UNSPECIFIED {
					return nil, status.Errorf(codes.InvalidArgument, "inner outer mask type has to be specified")
				}
			}
			idMap[tp.Id] = true