
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AproticSolventCompoundModule import AproticSolventCompound







class DiethyleneGlycolDiethylEther(AproticSolventCompound):
    """
    Class representing the `DiethyleneGlycolDiethylEther` entity, which inherits from:
    - AproticSolventCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_29ee50d4_27ed_4228_bd26_0010d9310f03'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DiethyleneGlycolDiethylEther'`
        - **Alias**: `class_name`
    
    - `IUPACName` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IUPACName`
    
    - `pubChemReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `pubChemReference`
    
    - `standardInChI` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `standardInChI`
    
    - `molecularFormula` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `molecularFormula`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = DiethyleneGlycolDiethylEther(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_29ee50d4_27ed_4228_bd26_0010d9310f03',
    
    class_name='DiethyleneGlycolDiethylEther',
    
    IUPACName="example_value",
    
    pubChemReference="example_value",
    
    standardInChI="example_value",
    
    molecularFormula="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_29ee50d4_27ed_4228_bd26_0010d9310f03',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DiethyleneGlycolDiethylEther',
        alias="class_name"
    )
    
    IUPACName: Optional[str] = Field(
        None,
        alias="IUPACName"
    )
    
    pubChemReference: Optional[str] = Field(
        None,
        alias="pubChemReference"
    )
    
    standardInChI: Optional[str] = Field(
        None,
        alias="standardInChI"
    )
    
    molecularFormula: Optional[str] = Field(
        None,
        alias="molecularFormula"
    )
    

    
    

    

    