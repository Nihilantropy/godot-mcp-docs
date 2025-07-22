# Support different actor locomotion {#doc_navigation_different_actor_locomotion}

![image](img/nav_actor_locomotion.png)

To support different actor locomotion like crouching and crawling, a
similar map setup as supporting
`doc_navigation_different_actor_types`{.interpreted-text role="ref"} is
required.

Bake different navigation meshes with an appropriate height for crouched
or crawling actors so they can find paths through those narrow sections
in your game world.

When an actor changes locomotion state, e.g. stands up, starts crouching
or crawling, query the appropriate map for a path.

If the avoidance behavior should also change with the locomotion e.g.
only avoid while standing or only avoid other agents in the same
locomotion state, switch the actor\'s avoidance agent to another
avoidance map with each locomotion change.

:::: tabs
.. code-tab:: gdscript GDScript

func update_path():

> 
>
> if actor_standing:
>
> :   path =
>     NavigationServer3D.map_get_path(standing_navigation_map_rid,
>     start_position, target_position, true)
>
> elif actor_crouching:
>
> :   path =
>     NavigationServer3D.map_get_path(crouched_navigation_map_rid,
>     start_position, target_position, true)
>
> elif actor_crawling:
>
> :   path =
>     NavigationServer3D.map_get_path(crawling_navigation_map_rid,
>     start_position, target_position, true)

func change_agent_avoidance_state():

> 
>
> if actor_standing:
>
> :   NavigationServer3D.agent_set_map(avoidance_agent_rid,
>     standing_navigation_map_rid)
>
> elif actor_crouching:
>
> :   NavigationServer3D.agent_set_map(avoidance_agent_rid,
>     crouched_navigation_map_rid)
>
> elif actor_crawling:
>
> :   NavigationServer3D.agent_set_map(avoidance_agent_rid,
>     crawling_navigation_map_rid)

::: code-tab
csharp
:::

private void UpdatePath() { if ([actorStanding]{#actorstanding}) {
[path]{#path} =
NavigationServer3D.MapGetPath([standingNavigationMapRid]{#standingnavigationmaprid},
[startPosition]{#startposition}, [targetPosition]{#targetposition},
true); } else if ([actorCrouching]{#actorcrouching}) { [path]{#path} =
NavigationServer3D.MapGetPath([crouchedNavigationMapRid]{#crouchednavigationmaprid},
[startPosition]{#startposition}, [targetPosition]{#targetposition},
true); } else if ([actorCrawling]{#actorcrawling}) { [path]{#path} =
NavigationServer3D.MapGetPath([crawlingNavigationMapRid]{#crawlingnavigationmaprid},
[startPosition]{#startposition}, [targetPosition]{#targetposition},
true); } }

private void ChangeAgentAvoidanceState() { if
([actorStanding]{#actorstanding}) {
NavigationServer3D.AgentSetMap([avoidanceAgentRid]{#avoidanceagentrid},
[standingNavigationMapRid]{#standingnavigationmaprid}); } else if
([actorCrouching]{#actorcrouching}) {
NavigationServer3D.AgentSetMap([avoidanceAgentRid]{#avoidanceagentrid},
[crouchedNavigationMapRid]{#crouchednavigationmaprid}); } else if
([actorCrawling]{#actorcrawling}) {
NavigationServer3D.AgentSetMap([avoidanceAgentRid]{#avoidanceagentrid},
[crawlingNavigationMapRid]{#crawlingnavigationmaprid}); } }
::::

:::: note
::: title
Note
:::

While a path query can be execute immediately for multiple maps, the
avoidance agent map switch will only take effect after the next server
synchronization.
::::
