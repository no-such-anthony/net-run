from .iterutils import remap, get_path, default_enter, default_visit

def remerge(target_list, sourced=False):
    """Takes a list of containers (e.g., dicts) and merges them using
    boltons.iterutils.remap. Containers later in the list take
    precedence (last-wins).
    By default, returns a new, merged top-level container. With the
    *sourced* option, `remerge` expects a list of (*name*, container*)
    pairs, and will return a source map: a dictionary mapping between
    path and the name of the container it came from.
    """

    if not sourced:
        target_list = [(id(t), t) for t in target_list]

    ret = None
    source_map = {}

    def remerge_enter(path, key, value):
        new_parent, new_items = default_enter(path, key, value)
        if ret and not path and key is None:
            new_parent = ret
        try:
            cur_val = get_path(ret, path + (key,))
        except KeyError:
            pass
        else:
            # TODO: type check?
            new_parent = cur_val

        if isinstance(value, list):
            # lists are purely additive. See https://github.com/mahmoud/boltons/issues/81
            #new_parent.extend(value)
            # modifed to extend at start rather than end, 
            # and maybe try to remove duplicates in correct order? Hope it works...
            new_parent = value + new_parent
            new_parent = list(dict.fromkeys(new_parent))
            new_items = []

        return new_parent, new_items

    for t_name, target in target_list:
        if sourced:
            def remerge_visit(path, key, value):
                source_map[path + (key,)] = t_name
                return True
        else:
            remerge_visit = default_visit

        ret = remap(target, enter=remerge_enter, visit=remerge_visit)

    if not sourced:
        return ret
    return ret, source_map