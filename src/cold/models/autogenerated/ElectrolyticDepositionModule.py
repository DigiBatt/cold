
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FormingFromIonisedModule import FormingFromIonised







class ElectrolyticDeposition(FormingFromIonised):
    """
    Class representing the `ElectrolyticDeposition` entity, which inherits from:
    - FormingFromIonised

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_a139c6d5_1a0b_4605_a6c0_9f383539f9b1'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectrolyticDeposition'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectrolyticDeposition(
    
    class_iri='https://w3id.org/emmo#EMMO_a139c6d5_1a0b_4605_a6c0_9f383539f9b1',
    
    class_name='ElectrolyticDeposition',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_a139c6d5_1a0b_4605_a6c0_9f383539f9b1',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectrolyticDeposition',
        alias="class_name"
    )
    

    
    

    

    