
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrolyteModule import Electrolyte







class SolidElectrolyte(Electrolyte):
    """
    Class representing the `SolidElectrolyte` entity, which inherits from:
    - Electrolyte

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0508a114_544a_4f54_a7de_9b947fb4b618'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SolidElectrolyte'`
        - **Alias**: `class_name`
    
    - `definition` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `definition`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SolidElectrolyte(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0508a114_544a_4f54_a7de_9b947fb4b618',
    
    class_name='SolidElectrolyte',
    
    definition="example_value",
    
    example="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0508a114_544a_4f54_a7de_9b947fb4b618',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SolidElectrolyte',
        alias="class_name"
    )
    
    definition: Optional[str] = Field(
        None,
        alias="definition"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    