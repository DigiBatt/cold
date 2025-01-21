
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DeterminationModule import Determination







class Observation(Determination):
    """
    Class representing the `Observation` entity, which inherits from:
    - Determination

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_3b19eab4_79be_4b02_bdaf_ecf1f0067a68'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Observation'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Observation(
    
    class_iri='https://w3id.org/emmo#EMMO_3b19eab4_79be_4b02_bdaf_ecf1f0067a68',
    
    class_name='Observation',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_3b19eab4_79be_4b02_bdaf_ecf1f0067a68',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Observation',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    