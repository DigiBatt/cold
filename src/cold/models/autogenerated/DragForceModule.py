
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ForceModule import Force



from .MechanicalQuantityModule import MechanicalQuantity







class DragForce(Force, MechanicalQuantity):
    """
    Class representing the `DragForce` entity, which inherits from:
    - Force, MechanicalQuantity

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_0dbdd7c5_86a5_4867_a396_2277e20fc4bc'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DragForce'`
        - **Alias**: `class_name`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `ISO80000Reference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ISO80000Reference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = DragForce(
    
    class_iri='https://w3id.org/emmo#EMMO_0dbdd7c5_86a5_4867_a396_2277e20fc4bc',
    
    class_name='DragForce',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    ISO80000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_0dbdd7c5_86a5_4867_a396_2277e20fc4bc',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DragForce',
        alias="class_name"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    ISO80000Reference: Optional[str] = Field(
        None,
        alias="ISO80000Reference"
    )
    

    
    

    

    