
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CoupledModule import Coupled







class TightlyCoupledModelsSimulation(Coupled):
    """
    Class representing the `TightlyCoupledModelsSimulation` entity, which inherits from:
    - Coupled

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_fbcc3aad_c58a_4185_bcc9_859db779b226'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'TightlyCoupledModelsSimulation'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = TightlyCoupledModelsSimulation(
    
    class_iri='https://w3id.org/emmo#EMMO_fbcc3aad_c58a_4185_bcc9_859db779b226',
    
    class_name='TightlyCoupledModelsSimulation',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_fbcc3aad_c58a_4185_bcc9_859db779b226',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'TightlyCoupledModelsSimulation',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    

    

    