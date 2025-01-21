
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .NumberOfFiniteVolumeCellsModule import NumberOfFiniteVolumeCells







class NumberOfFiniteVolumeCellsInX(NumberOfFiniteVolumeCells):
    """
    Class representing the `NumberOfFiniteVolumeCellsInX` entity, which inherits from:
    - NumberOfFiniteVolumeCells

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_e73586eb_8475_4879_a43e_087c702ea6bf'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'NumberOfFiniteVolumeCellsInX'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = NumberOfFiniteVolumeCellsInX(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_e73586eb_8475_4879_a43e_087c702ea6bf',
    
    class_name='NumberOfFiniteVolumeCellsInX',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_e73586eb_8475_4879_a43e_087c702ea6bf',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'NumberOfFiniteVolumeCellsInX',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    