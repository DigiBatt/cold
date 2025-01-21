
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrodePolarisationModule import ElectrodePolarisation







class AnodicPolarisation(ElectrodePolarisation):
    """
    Class representing the `AnodicPolarisation` entity, which inherits from:
    - ElectrodePolarisation

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_28213033_4c74_441c_81c4_a0cad05f9eb6'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AnodicPolarisation'`
        - **Alias**: `class_name`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AnodicPolarisation(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_28213033_4c74_441c_81c4_a0cad05f9eb6',
    
    class_name='AnodicPolarisation',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_28213033_4c74_441c_81c4_a0cad05f9eb6',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AnodicPolarisation',
        alias="class_name"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    