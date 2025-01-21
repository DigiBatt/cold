
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .MultiSimulationModule import MultiSimulation







class Coupled(MultiSimulation):
    """
    Class representing the `Coupled` entity, which inherits from:
    - MultiSimulation

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_02c4890b_aef3_4173_9669_94d1f6baf611'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Coupled'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Coupled(
    
    class_iri='https://w3id.org/emmo#EMMO_02c4890b_aef3_4173_9669_94d1f6baf611',
    
    class_name='Coupled',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_02c4890b_aef3_4173_9669_94d1f6baf611',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Coupled',
        alias="class_name"
    )
    

    
    

    

    