
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectricChargeModule import ElectricCharge



from .SIExactConstantModule import SIExactConstant







class ElectronCharge(ElectricCharge, SIExactConstant):
    """
    Class representing the `ElectronCharge` entity, which inherits from:
    - ElectricCharge, SIExactConstant

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_cc01751d_dd05_429b_9d0c_1b7a74d1f277'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectronCharge'`
        - **Alias**: `class_name`
    
    - `definition` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `definition`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectronCharge(
    
    class_iri='https://w3id.org/emmo#EMMO_cc01751d_dd05_429b_9d0c_1b7a74d1f277',
    
    class_name='ElectronCharge',
    
    definition="example_value",
    
    iupacReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_cc01751d_dd05_429b_9d0c_1b7a74d1f277',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectronCharge',
        alias="class_name"
    )
    
    definition: Optional[str] = Field(
        None,
        alias="definition"
    )
    
    iupacReference: Optional[str] = Field(
        None,
        alias="iupacReference"
    )
    

    
    

    

    