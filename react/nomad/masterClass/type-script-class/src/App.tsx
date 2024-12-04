import { DragDropContext, Draggable, Droppable } from "react-beautiful-dnd";

function App() {
  const onDragEnd = () => {};

  // DragDropContext should get some children
  // Droppable should get some children as function
  // They also should get id
  return (
    <DragDropContext onDragEnd={onDragEnd}>
      <div>
        <Droppable droppableId="one">
          {(provided) => (
            <ul ref={provided.innerRef} {...provided.droppableProps}>
              <Draggable draggableId="first" index={0}>
                {(provided) => (
                  <li ref={provided.innerRef} {...provided.draggableProps}>
                    <span {...provided.dragHandleProps}>🧖</span>
                    One
                  </li>
                )}
              </Draggable>
              <Draggable draggableId="second" index={1}>
                {(provided) => (
                  <li ref={provided.innerRef} {...provided.draggableProps}>
                    <span {...provided.dragHandleProps}>🧖</span>
                    Two
                  </li>
                )}
              </Draggable>
            </ul>
          )}
        </Droppable>
      </div>
    </DragDropContext>
  );
}

export default App;
