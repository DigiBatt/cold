
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectricImpedanceModule import ElectricImpedance







class ImaginaryElectricImpedance(ElectricImpedance):
    """
    Class representing the `ImaginaryElectricImpedance` entity, which inherits from:
    - ElectricImpedance

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0089729b_5890_4c15_aa09_1244d41f8626'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ImaginaryElectricImpedance'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ImaginaryElectricImpedance(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0089729b_5890_4c15_aa09_1244d41f8626',
    
    class_name='ImaginaryElectricImpedance',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_0089729b_5890_4c15_aa09_1244d41f8626',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ImaginaryElectricImpedance',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    