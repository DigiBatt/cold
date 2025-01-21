
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .EstimationModule import Estimation



from .ComputationModule import Computation







class Simulation(Estimation, Computation):
    """
    Class representing the `Simulation` entity, which inherits from:
    - Estimation, Computation

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_9335cf09_431f_4613_9dab_ce4ceaca965b'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Simulation'`
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
    obj = Simulation(
    
    class_iri='https://w3id.org/emmo#EMMO_9335cf09_431f_4613_9dab_ce4ceaca965b',
    
    class_name='Simulation',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_9335cf09_431f_4613_9dab_ce4ceaca965b',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Simulation',
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
    

    
    

    

    