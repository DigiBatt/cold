
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectricImpedanceModule import ElectricImpedance







class RealElectricImpedance(ElectricImpedance):
    """
    Class representing the `RealElectricImpedance` entity, which inherits from:
    - ElectricImpedance

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_abf986d2_90d5_4746_b42b_89dc7cc1bf0f'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'RealElectricImpedance'`
        - **Alias**: `class_name`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = RealElectricImpedance(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_abf986d2_90d5_4746_b42b_89dc7cc1bf0f',
    
    class_name='RealElectricImpedance',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_abf986d2_90d5_4746_b42b_89dc7cc1bf0f',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'RealElectricImpedance',
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
    

    
    

    

    